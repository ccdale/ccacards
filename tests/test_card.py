import pytest

from ccacards.card import Card


def test_Card():
    c = Card(14)  # Ace of Hearts
    assert c.value == 0
    assert c.valuename == "Ace"
    assert str(c) == "Ace of Hearts"


def test_Card_maths():
    c = Card(46)  # 7 of clubs
    assert c.value == 6
    assert c.valuename == "Seven"
    assert str(c) == "Seven of Clubs"


def test_Card_Zero():
    c = Card(0)  # Blank, non-existent card
    assert c.value == 0
    assert c.valuename == "Blank"
    assert str(c) == "Blank of Blank"


def test_Card_facedown():
    c = Card(14, facedown=True)  # Ace of Hearts
    assert c.value == 0
    assert c.valuename == "Ace"
    assert str(c) == "Face Down"
    c.flip()  # Flip it over
    assert str(c) == "Ace of Hearts"


def test_Card_repr_and_imagefile():
    c = Card(14)
    assert repr(c) == "Card(14)"
    assert c.imagefile.name == "14.png"


@pytest.mark.parametrize("bad_index", [-1, 53])
def test_Card_index_out_of_range_raises(bad_index):
    with pytest.raises(ValueError):
        Card(bad_index)
