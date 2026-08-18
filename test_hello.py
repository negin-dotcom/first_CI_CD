from hello import say_hello


def test_say_hello_world_default():
    assert say_hello() == "Hello, World!"


def test_say_hello_custom():
    assert say_hello("Mentor") == "Hello, Mentor!"


def test_say_hello_empty():
    assert say_hello("") == "Hello, !"


