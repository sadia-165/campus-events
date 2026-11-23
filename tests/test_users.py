import pytest
from app.users import UserService


def test_register_normalises_email(conn):
    s = UserService(conn)
    s.register(" Ana ", " ANA@Mail.com ")
    assert s.list()[0]["email"] == "ana@mail.com"


def test_duplicate_email_rejected(conn):
    s = UserService(conn)
    s.register("A", "a@x.com")
    with pytest.raises(ValueError):
        s.register("B", "a@x.com")


@pytest.mark.parametrize("n,e", [("", "a@x.com"), ("A", "nope")])
def test_invalid_input(conn, n, e):
    with pytest.raises(ValueError):
        UserService(conn).register(n, e)
