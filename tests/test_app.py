from app import index


def test_index():
    assert index() == "Hello, world!"


def test_add():
    assert (1 + 1) == 2