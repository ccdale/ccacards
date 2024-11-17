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
