from typing import List
import random

# Handler class for decks of cards. on instantation, generate how every many decks mixed in together, from 1-4. most real casios use 4+
class Deck:
    def __init__(self, num_decks=1):
        
        # Generate a deck
        deck: List[str] = []
        suites = ["d", "c", "h", "s"]
        
        for i in range(num_decks):
            # each suite is generated one at a time and appended to decks list
            for suite in suites:
                # add ace for suite
                deck.append(f"a-{suite}")
                # add face cards for suite
                deck.append(f"j-{suite}")
                deck.append(f"k-{suite}")
                deck.append(f"q-{suite}")
                # add 2-10 number cards
                for i in range(2, 11, 1):
                    deck.append(f"{i}-{suite}")

        # shuffle built deck
        random.shuffle(deck)

        # load deck into self instance
        self.__deck = deck
    
    def draw_card(self) -> str:
        """Draw a card from the deck and return the str representation. card is removed from deck until reshuffled."""
        card = self.__deck.pop(-1)
        self.__discard = card

        return card

    # no shuffle method is needed, new deck instantated on every round