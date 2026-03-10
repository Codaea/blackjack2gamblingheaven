from deck import Deck
from util import clear_screen, star_break, validate_bool, ascii_back, ascii_card, get_card_values

def start_blackjack(bank: float) -> float:
    """game manager for blackjack from menu. takes current money as the input, returns the new money after gambling """

    print("Welcome to blackjack!")
    # play a round of blackjack
    bank = single_round(bank, 1, 5)
    star_break()
    print(f"Thanks for playing blackjack! you have ${bank}.")
    while True:
        again = validate_bool("Do you want to play again? (Y or N): ")
        if not again:
            break
        bank = single_round(bank, 1, 5)
        print(f"Thanks for playing blackjack! you have ${bank}.")
    return bank

def single_round(bank: float, decks: int, buy_in: int) -> float:
    """Handle a single table for 1 iteration/game, bank is current money, decks is how many decks are in the shuffle deck. buy in is cost to play return how much money they have after playing, including wins and losses"""
    # make a new deck of cards to play with. 6(52 card) decks is the standard for a game in a casino (to prevent counting!)
    pot = 0
    deck = Deck(6)
    
    # Shuffle the deck before starting
    
    # Tell player buy in, ask if they want to play, declines send them back to menu
    clear_screen()
    star_break()
    choice = validate_bool(f"The buy in is ${buy_in}. Would you like to play? (Yes/No) ")
    
    if choice == False:
        return bank # They chose to not play, send them back to game manager
    
    # Don't allow them to play if they don't have any money
    if bank < buy_in:
        print("What are you doing? You cannot afford this table!")
        return bank

    # take their buy in, and place it in the pot
    bank -= buy_in
    pot += buy_in

    # ask how much they want to bet
    bet = int(input(f"You have ${bank} left. How much do you want to bet? (Enter a number between 1 and {bank}) "))
    while bet < 1 or bet > bank:
        bet = int(input(f"Invalid bet. Enter a number between 1 and {bank}: "))

    # remove from bank, add to pot
    bank -= bet
    pot += bet

    # deal two cards to player
    player_cards = [deck.draw_card(), deck.draw_card()]
    
    # deal two cards to dealer
    dealer_cards = [deck.draw_card(), deck.draw_card()]

    clear_screen()
    star_break()
    print("Dealer:")
    print(ascii_back())
    print(ascii_card(dealer_cards[1])) # shows second card
    print(f"Value: {get_card_values([dealer_cards[1]])}")
    # show user their cards
    
    star_break()
    print("You:")
    for card in player_cards:
        print(ascii_card(card))
    print(f"Value: {get_card_values(player_cards)}")
    
    # if player already have 21, they win immediately
    if get_card_values(player_cards) == 21:
        print("Blackjack! You win!")
        bank += pot * 2.5 # blackjack pays 3:2, so they get their money back plus 1.5x their bet
        return bank
    
    # give player option to hit or stay
    choice = input("Hit or stay? (hit enter to hit, type anything else to stay) ")

    hit = choice.strip().lower()[:1] == "h" # True if hit
    
    if hit:
        # hit, draw a card for player
        player_cards.append(deck.draw_card())
        clear_screen()
        star_break()
        print("You:")
        for card in player_cards:
            print(ascii_card(card))
        print(f"Value: {get_card_values(player_cards)}")
        if get_card_values(player_cards) > 21:
            print("Bust! You lose.")
            return bank # they lost, return their money with no changes

    # player stays, now its dealers turn. reveal hole card
    print("Dealer:")
    for card in dealer_cards:
        print(ascii_card(card))
    print(f"Value: {get_card_values(dealer_cards)}")
    
    # dealer hits until they have 17 or more
    while get_card_values(dealer_cards) < 17:
        print("Dealer hits.")
        dealer_cards.append(deck.draw_card())
        print("Dealer:")
        for card in dealer_cards:
            print(ascii_card(card))
        print(f"Value: {get_card_values(dealer_cards)}")
    
    
    # check who won
    player_value = get_card_values(player_cards)
    dealer_value = get_card_values(dealer_cards)
    
    if dealer_value > 21:
        print("Dealer busts! You win!")
        bank += pot  # Player gets their bet back
        bank += pot  # Player wins the pot
    elif dealer_value > player_value:
        print("Dealer wins! You lose.")
        # No changes to bank, player loses their bet
    elif dealer_value < player_value:
        print("You win!")
        bank += pot  # Player gets their bet back
        bank += pot  # Player wins the pot
    else:
        print("Push! It's a tie.")
        bank += pot  # Player gets their bet back only

    print(f"You made ${pot}!")
    return bank