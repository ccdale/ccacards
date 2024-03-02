import sys

from ccaerrors import errorExit, errorNotify, errorRaise
import ccalogging

log = ccalogging.log


class Stack:
    """Representation of a Stack of Playing Cards."""

    def __init__(self):
        """Initialises an empty Stack."""
        try:
            self.cards = []
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __repr__(self):
        """Placeholder repr(Stack) function."""
        try:
            return f"Stack()"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __str__(self):
        """Placeholder str(Stack) function. LIFO ordering."""
        try:
            return str([str(c) for c in reversed(self.cards)])
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __len__(self):
        """returns the length of this Stack."""
        try:
            return len(self.cards)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def append(self, card):
        """Adds a card to the top of this Stack."""
        try:
            self.cards.append(card)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def pop(self):
        """Removes the top card and returns it, or None if Stack is empty."""
        try:
            if len(self) > 0:
                return self.cards.pop()
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def peek(self):
        """Returns the top card without removing it from the Stack, or None if Stack is empty."""
        try:
            if len(self) > 0:
                return self.cards[-1]
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)


if __name__ == "__main__":
    # ccalogging.setDebug()
    # ccalogging.setConsoleOut()
    # log.info("Stack object.")
    s = Stack()
    [s.append(c) for c in range(1, 11)]
    print(s)
    print(f"pop: {s.pop()}")
    print(f"pop: {s.pop()}")
    print(f"pop: {s.pop()}")
    print(f"peek: {s.peek()}")
    print(s)
