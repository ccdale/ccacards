from random import shuffle
import sys

from ccaerrors import errorExit, errorNotify, errorRaise
import ccalogging

from ccacards.card import Card
from ccacards.stack import Stack

log = ccalogging.log


class Deck(Stack):
    """Representation of a Deck of Playing Cards."""

    def __init__(self, pullaces=False, shuffleaces=True):
        """Initialises a Deck of 52 playing cards.

        Extracts the Aces into a seperate list if pullaces is True
        Randomises the order of the list of Aces if shuffleaces is True
        """
        try:
            self.cards = [Card(c) for c in range(1, 53)]
            self.aces = None
            if pullaces:
                self.aces = []
                acepos = [i for i in range(0, 52, 13)]
                # we need to pull the aces in reverse order
                # as when we pop each of them off the deck
                # all the cards change position by 1
                acepos.reverse()
                for i in acepos:
                    self.aces.append(self.cards.pop(i))
                if shuffleaces:
                    # randomise the order of the aces
                    shuffle(self.aces)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def shuffle(self, times=1):
        try:
            for i in range(times):
                shuffle(self.cards)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def deall(self, number=1):
        """Deals <number> of cards from the top of the deck

        returns a list of Card() objects.
        """
        try:
            number = min(number, len(self.cards))
            if number > 0:
                return [self.pop() for _ in range(number)]
            return []
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def deal(self, number=1):
        """Deals <number> of cards from the top of the deck.

        If number is 1 then returns a Card() object else
        returns a list of Card() objects.
        """
        try:
            dlist = self.deall(number=number)
            if number == 1:
                return dlist.pop()
            return dlist
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)
