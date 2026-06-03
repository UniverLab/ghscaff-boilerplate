from src.core import hello


def test_hello_default() -> None:
    assert hello() == "Hello from {{name}}, world!"


def test_hello_custom() -> None:
    assert hello("test") == "Hello from {{name}}, test!"
