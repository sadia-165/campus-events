import pytest
from app.events import EventFactory, EventRepository, EventService


def test_factory_workshop():
    assert EventFactory.create("workshop", "Git", 10, tool="Git")["extra"] == "Git"


@pytest.mark.parametrize("args,kw", [(("workshop", "T", 5), {}), (("seminar", "T", 5), {}),
                                     (("podcast", "T", 5), {}), (("seminar", " ", 5), {"speaker": "x"}),
                                     (("seminar", "T", 0), {"speaker": "x"})])
def test_factory_rejects_bad_input(args, kw):
    with pytest.raises(ValueError):
        EventFactory.create(*args, **kw)


def test_service_persists(conn):
    repo = EventRepository(conn)
    eid = EventService(repo).create("seminar", "AI", 50, speaker="Dr. X")
    assert repo.get(eid)["title"] == "AI"
    assert repo.get(999) is None
