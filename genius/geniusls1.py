from calcGen import add


def test_add():
    assert add(1, 2 ) == 3
    assert add(1, 3 ) == 4
    assert add(1, 0 ) == 1
    assert add(-1, 1 ) == 0

