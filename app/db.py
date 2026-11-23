import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL);
CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, kind TEXT, title TEXT, capacity INTEGER, extra TEXT);
CREATE TABLE IF NOT EXISTS registrations(id INTEGER PRIMARY KEY, event_id INTEGER, user_id INTEGER,
    status TEXT, UNIQUE(event_id, user_id));
CREATE TABLE IF NOT EXISTS feedback(id INTEGER PRIMARY KEY, event_id INTEGER, user_id INTEGER,
    rating INTEGER, comment TEXT);
"""


def connect(path="events.db"):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn
