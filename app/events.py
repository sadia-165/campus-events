"""Events module. PATTERN: Factory (EventFactory + BUILDERS registry)."""
BUILDERS = {}


def builder(kind):
    def register(fn):
        BUILDERS[kind] = fn
        return fn
    return register


@builder("workshop")
def _workshop(title, capacity, **kw):
    if not kw.get("tool"):
        raise ValueError("workshop needs a tool")
    return {"kind": "workshop", "title": title, "capacity": capacity, "extra": kw["tool"]}


@builder("seminar")
def _seminar(title, capacity, **kw):
    if not kw.get("speaker"):
        raise ValueError("seminar needs a speaker")
    return {"kind": "seminar", "title": title, "capacity": capacity, "extra": kw["speaker"]}


class EventFactory:
    @staticmethod
    def create(kind, title, capacity, **kw):
        if kind not in BUILDERS:
            raise ValueError(f"unknown event kind: {kind}")
        if not title.strip():
            raise ValueError("title required")
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        return BUILDERS[kind](title.strip(), capacity, **kw)


class EventRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, d):
        cur = self.conn.execute(
            "INSERT INTO events(kind, title, capacity, extra) VALUES(?,?,?,?)",
            (d["kind"], d["title"], d["capacity"], d["extra"]))
        self.conn.commit()
        return cur.lastrowid

    def get(self, event_id):
        r = self.conn.execute("SELECT * FROM events WHERE id=?", (event_id,)).fetchone()
        return dict(r) if r else None


class EventService:
    def __init__(self, repo):
        self.repo = repo

    def create(self, kind, title, capacity, **kw):
        return self.repo.add(EventFactory.create(kind, title, capacity, **kw))
