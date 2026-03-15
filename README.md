# Blackjack 2: Gambling heaven

Lane CC CS 161P Final Project

A text based game, with a virtual casino. You can take out loans, bet your house on roulette, and play blackjack.

Make your wildest dreams come true, or lose it all. The choice is yours.

## How to run

### In a terminal

1. Go to the project root directory.

2. Run the program.

```sh
   python main.py
```

---

## Videos

- [Code Demo](https://youtu.be/E2AnXw3WRx4)
- [Code Walkthrough](https://youtu.be/rfb25c4jQ1E)

---

## Citations

This project uses the following libraries and assets.

| Library / Asset | License Type   | Usage   |
| :- | :- | :- |
| [Ascii_cards](https://github.com/naivoder/ascii_cards/tree/main) | MIT | Borrowed card design |

## To Do

- [x] Implement blackjack game
  - [x] Card deck handling with mechanics, for real shuffle of cards (deck object with methods for drawing a card, returning it, then placing it into a discard list. discard list gets shuffled back into the deck when the deck is empty or frontend calls for a reshuffle)
        -  [x] Deck class
            - [X] initialize deck method
            - [X] draw method
            - [X] discard pile handling
  - Add a ability to teach how to count cards? (Shop with cool glasses for 100$ that add a card counting ability to your player)
  card generation function that can return a text ascii text based on input values
  - [ ] rollette
- [ ] Implement loan system
- [ ] bips and ends
- [x] save progress in game file (json or text file?)
- [ ] convert cards from text to object, cards can handle string methods directly then along with summation beinh handled by a "Hand" class that can hold a list of cards.

if I have time we should re-implement the blackjack game with a more consistent UI that is rebuilt every time, with a more consistent HUD.
