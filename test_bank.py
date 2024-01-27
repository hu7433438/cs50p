from bank import value

def test_hello():
    assert value('hello') == 0


def test_hello_upper():
    assert value('Hello') == 0


def test_h():
    assert value('hero') == 20


def test_w():
    assert value('world') == 100

