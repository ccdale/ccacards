import sys

from ccaerrors import errorExit, errorNotify, errorRaise
import ccalogging

log = ccalogging.log


class Card:
    """Representation of a Playing Card."""

    valueNames = [
        "Ace",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
    ]

    suitNames = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self, index, facedown=False):
        """Initialises the Card

        args:
            index: int 0 - 52
                0 is a placeholder for 'no card' i.e. blank space
                1 == Ace of Spades
                13 == King of Spades
                14 == Ace of Hearts
                26 == King of Hearts
                27 == Ace of Diamonds
                39 == King of Diamonds
                40 == Ace of Clubs
                52 == King of Clubs
        """
        try:
            self.facedown = facedown
            self.index = index
            if self.index == 0:
                self.value = 0
                self.valuename = "Blank"
                self.suit = "Blank"
            else:
                self.suitindex, self.value = divmod(self.index - 1, 13)
                self.valuename = self.valueNames[self.value]
                self.suit = self.suitNames[self.suitindex]
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __str__(self):
        try:
            return "Face Down" if self.facedown else f"{self.valuename} of {self.suit}"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __repr__(self):
        try:
            return f"Card({self.index})"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)
