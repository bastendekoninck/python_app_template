from app.main import say_hello


def test_say_hello() -> None:
    assert say_hello("Alice") == "Hello, Alice!"
