from unittest.mock import Mock
from app.observers import EventBus, NotificationObserver, ConsoleNotifier


def test_failing_observer_isolated():
    bus, good = EventBus(), Mock()
    bus.subscribe("t", Mock(side_effect=RuntimeError))
    bus.subscribe("t", good)
    bus.publish("t", {"x": 1})
    good.assert_called_once_with({"x": 1})


def test_notification_observer_uses_notifier():
    n = Mock()
    NotificationObserver(n, "Hi")({"email": "a@x.com", "event_id": 1, "status": "confirmed"})
    n.send.assert_called_once()


def test_console_notifier_prints(capsys):
    ConsoleNotifier().send("a@x.com", "S", "B")
    assert "a@x.com" in capsys.readouterr().out


def test_publish_without_subscribers():
    EventBus().publish("none", {})
