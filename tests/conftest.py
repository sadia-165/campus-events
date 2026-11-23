import pytest
from app.db import connect


@pytest.fixture
def conn():
    return connect(":memory:")
