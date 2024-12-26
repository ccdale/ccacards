from ccacards.deck import Deck


def test_Deck():
    d = Deck()
    c = d.deal()
    assert len(d) == 51
    assert c.value == 12
    assert str(c) == "King of Clubs"


def test_Deck_noaces():
    d = Deck(pullaces=True)
    assert len(d) == 48
    xc = d.deal(13)
    assert str(xc[-1]) == "King of Diamonds"
    assert str(xc[0]) == "King of Clubs"


def test_Deck_deall():
    d = Deck()
    c = d.deall(5)
    assert len(d) == 47
    assert str(c[-1]) == "Nine of Clubs"
    assert str(c[0]) == "King of Clubs"
