# Flip Out

In a moment of madness, you have decided coding challenges are not enough, and so you have decided to play a card game.

This game consists of dealing out a random number of cards (from any number of decks), which have been mixed to include face-up (1) and face-down (0) cards. A deal from the deck might look like this:

```txt
1010010b
```

Each step of the game involves removing a face-up card and flipping over any cards immediately adjacent to it. The empty space left behind is never refilled. The game ends when the cards have either been removed entirely (in which case, you win!) or no valid moves remain.

A simple game could progress like so, with a "." in place of a removed card:

```txt
11010
111.1
10..1
.1..1
....1
.....
```

The game ends in 5 turns, after which there are no cards left. The game could also end in failure:

```txt
11010
0.110
0..00
```

Here, removing the second card leaves the first in a state where it can be neither moved nor flipped. Of the three starting face-up cards, either the left-most or right-most could be chosen while leaving the game in a state where it can be won.

Naturally, you have decided to solve this game - or at least the first step. With a set of dealt hands each represented by a single line of face-up or face-down cards, you can find out how many cards are valid first moves. For example:

```txt
11010        -> 2 (positions 0, 3)
110          -> 0
00101011010  -> 3 (positions 2, 6, 9)
```

For a total of 5 valid starting positions for the set.
Treating your input as a set of dealt hands, work out how many valid starting positions are in that set.
