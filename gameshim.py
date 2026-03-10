from blackjack import start_blackjack, single_round

# Start from blackjack screen with 500 money
# start_blackjack(500)

# Start single blackjack game
bank = single_round(500, 1, 5)
print(f"Your final bankroll is: ${bank}")