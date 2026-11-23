import sqlite3


class UserService:
    def __init__(self, conn):
        self.conn = conn

    def register(self, name, email):
        name, email = name.strip(), email.strip().lower()
        if not name or "@" not in email:
            raise ValueError("valid name and email required")
        try:
            cur = self.conn.execute("INSERT INTO users(name, email) VALUES(?, ?)", (name, email))
        except sqlite3.IntegrityError:
            raise ValueError("email already registered")
        self.conn.commit()
        return cur.lastrowid

    def list(self):
        return [dict(r) for r in self.conn.execute("SELECT * FROM users")]
