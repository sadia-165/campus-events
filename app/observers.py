"""Notifications module. PATTERN: Observer (EventBus + observers)."""


class ConsoleNotifier:
    def send(self, to, subject, body):
        print(f"[mail to {to}] {subject}: {body}")


class EventBus:
    def __init__(self):
        self._subs = {}

    def subscribe(self, topic, observer):
        self._subs.setdefault(topic, []).append(observer)

    def publish(self, topic, payload):
        for obs in self._subs.get(topic, []):
            try:
                obs(payload)
            except Exception:  # one failing observer must not stop the others
                pass


class NotificationObserver:
    def __init__(self, notifier, subject):
        self.notifier, self.subject = notifier, subject

    def __call__(self, payload):
        self.notifier.send(payload["email"], self.subject, f"Event #{payload['event_id']}: {payload['status']}")
