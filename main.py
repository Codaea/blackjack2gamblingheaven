# Blackjack 2: Gambling Heaven
# A text based gambling game where you can play blackjack, roulette, take out loans, and more. The goal is to make as much money as possible before you run out of money or get bored and quit.
# @Codaea
# 3/15/2026
from util import clear_screen, star_break
from blackjack import start_blackjack

print("Welcome To Blackjack 2: Gambling Heaven!")

name = input("What is your gambling name?\n")
# Handle edgecase of just clicking enter past
while name == '':
    name = input("Please input a valid name.\n")
clear_screen()

# Welcome Message

day = 0
bank = 500
# Main game loop
while True:
    star_break()
    print(f"Welcome {name}, to the casino of your dreams.\nMake your wildest dreams come true, or lose it all. The choice is yours.")
    star_break()
    print("\n\n")

    print("""On the casino floor, there are many ways to go.
      1: Play blackjack
      2: save progress
      3: load progress
      """)

    # no validation because idgaf
    # day autoincrements each time they pick a option from the main menu. its what loans are based off of.
    choice = int(input("Choose a option: "))
    day+= 0

    # Blackjack table
    if choice == 1:
        bank = start_blackjack(bank) # start blackjack, it returns new bank value after game is over
    elif choice == 2:
        # save progress
        with open("game.sav", "w") as file:
            # bank on line 1, day on line 2
            file.write(f"{bank}\n{day}")
            file.close()
        print("Game Saved!")
    elif choice == 3:
        try:
            with open("game.sav", "r") as file:
                s = file.read()
                s = s.split()

                bank = float(s[0])
                day = float(s[1])

                print(f"Loaded Save! Bank: {bank} Day: {day}")
        except FileNotFoundError:
            print("Unable to load save! File not found!")
        
    else:
        print("That option is not avalible")


    print(f"you have ${bank}")
