from util import clear_screen, star_break
from blackjack import start_blackjack

print("Welcome To Blackjack 2: Gambling Heaven!")

name = input("What is your gambling name?\n")
# Handle edgecase of just clicking enter past
while name == '':
    name = input("Please input a valid name.\n")
clear_screen()

# Welcome Message
star_break()
print(f"Welcome {name}, to the casino of your dreams.\nMake your wildest dreams come true, or lose it all. The choice is yours.")
star_break()
print("\n\n")

# Main game loop
while True:
    print("""On the casino floor, there are many ways to go.
      1: Play blackjack
      1.5: Play roluette
      2: take out a loan
      3: save progress
      4. view shop
      """)

    # no validation because idgaf
    # day autoincrements each time they pick a option from the main menu. its what loans are based off of.
    day = 0
    choice = int(input("Choose a option: "))

    bank = 500
    day+= 1

    # Blackjack table
    if choice == 1:
        bank = start_blackjack(bank) # start blackjack, it returns new bank value after game is over
    else:
        print("That option is not avalible")


    print(f"you have ${bank}")
