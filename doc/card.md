# card object

## Description

Representation of a Playing Card as a Python object.

## Methods

* `__init__(index, facedown=False)`

    Initialises the Card

    `c = Card(1) # Ace of Spades`

    args:
        `index`: int 0 - 52

```
          0 is a placeholder for 'no card' i.e. blank space
          1 == Ace of Spades
         13 == King of Spades
         14 == Ace of Hearts
         26 == King of Hearts
         27 == Ace of Diamonds
         39 == King of Diamonds
         40 == Ace of Clubs
         52 == King of Clubs
```

## Properties

* `suit`
    Returns the string name of the card suit

* `value`
    Returns the value of the card 1 - 13

* `valuename`
    Returns the string name of the card value

* `facedown`
    Returns True if the card is face down

* `imagefile`
    Returns the path to the image file for this card
