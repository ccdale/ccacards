from ccacards.stack import Stack


def test_Stack():
    s = Stack()
    [s.append(c) for c in range(1, 11)]
    xs = str(s)
    expected = "['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']"
    assert expected == xs


def test_Stack_pop():
    s = Stack()
    [s.append(c) for c in range(1, 11)]
    expected = "10"
    xs = str(s.pop())
    assert expected == xs
    expected = "['9', '8', '7', '6', '5', '4', '3', '2', '1']"
    xs = str(s)
    assert expected == xs


def test_Stack_peek():
    s = Stack()
    [s.append(c) for c in range(1, 11)]
    expected = "10"
    xs = str(s.peek())
    assert expected == xs
    xs = str(s)
    expected = "['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']"
    assert expected == xs


def test_empty_Stack():
    s = Stack()
    expected = None
    xs = s.peek()
    assert expected == xs
    xs = s.pop()
    assert expected == xs
