import os
from typing import List

def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS (posix)
        _ = os.system('clear')

def get_term_col() -> int:
    term_size = os.get_terminal_size()
    return term_size.columns
    

def star_break() -> None:
    """Print star **** break between lines"""
    print("*" * get_term_col())

def validate_bool(input_str: str) -> bool:
    """Asks user for input, and doesn't return until y or n is supplied. y is true, n is false"""
    x: str = input(input_str).strip().lower()[:1] # get first character, strip whitespace, and lowercase it

    # Forced loop until y or n achieved
    while x != "y" and x != "n":
        x = input("Invalid input. Only Y or N accepted: ").strip().lower()

    return x == "y"


# Card utils

def ascii_card(card: str) -> str:
    """return str of a ascii card art for the specified card"""
    # cards are stored as a-s for ace of spades
    card_parts = card.split("-")

    rank = card_parts[0] # the first part of card
    suite = card_parts[1] # the suite

    # make the rank bigger for card insertion
    rank = rank.capitalize()
    
    # reassign suite to icon
    if suite == "d":
        suite = "♦"
    elif suite == "c":
        suite = "♣"
    elif suite == "h":
        suite = "♥"
    else: # suite must be spades is final case
        suite = "♠"
    
    
    # art borrowed from https://github.com/naivoder/ascii_cards/blob/main/ascii_cards/cards.py
    card = "┌─────────┐\n"
    card +=f"│{suite}        │\n"
    card +=f"│{rank}      {'' if len(rank) == 2 else ' '} │\n" # little inline if handles spacing if rank is more than 1 character
    card +="│         │\n"
    card +="│         │\n"
    card +="│         │\n"
    card +="└─────────┘"

    return card

def ascii_back() -> str:
    """returns str for the back of a ascii card"""
    card =  "┌─────────┐\n"
    card += "│/////////│\n"
    card += "│/////////│\n"
    card += "│/////////│\n"
    card += "│/////////│\n"
    card += "│/////////│\n"
    card += "└─────────┘"

    return card
    
def get_card_values(cards: List[str]) -> int:
    """return int value of the cards supplied, for adding to 21"""
    running_total = 0
    ace_count = 0
    
    # we handle in order of face, then rank, and last aces because they can be 11 or 1
    for card in cards:
        # cards are stored as a-s for ace of spades
        card = card.split("-")
        
        rank = card[0] # the first part of card
        suite = card[1] # the suite

        # aces are handled later from seperate list because of 11 V 1
        if rank == 'a':
            ace_count += 1

        # handling face cards
        elif rank == "j" or rank == "k" or rank == "q":
            running_total += 10
        
        # must be a 2-10 card, convert str to int and add to running total
        else:
            running_total += int(rank)

    # Aces are worth either 11 or 1, assume 11 unless that would mean bust combined with other cards, otherwise just 1
    # this code is really neat, and solves the issue.

    running_total += ace_count * 11  # assume all aces are worth 11 initially

    while running_total > 21 and ace_count > 0:
        running_total -= 10  # Convert one ace from 11 to 1
        ace_count -= 1

    return running_total