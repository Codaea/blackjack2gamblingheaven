# Blackjack 2: Gambling heaven

Lane CC CS 161P Final Project

A text based game, with a virtual casino. You can take out loans, bet your house on roulette, and play blackjack.

Make your wildest dreams come true, or lose it all. The choice is yours.

## How to run

1. Clone the repository
2. Run `python main.py` in the terminal
3. Follow the prompts to play the game

## To Do

- [x] Implement blackjack game
  - [x] Card deck handling with mechanics, for real shuffle of cards (deck object with methods for drawing a card, returning it, then placing it into a discard list. discard list gets shuffled back into the deck when the deck is empty or frontend calls for a reshuffle)
        -  ] Deck class 
            - [X] initialize deck method
            - [X] draw method
            - [X] discard pile handling
  - Add a ability to teach how to count cards? (Shop with cool glasses for 100$ that add a card counting ability to your player)
  card generation function that can return a text ascii text based on input values
  - [ ] rollette
- [ ] Implement loan system
- [ ] bips and ends
- [ ] save progress in game file (json or text file?)