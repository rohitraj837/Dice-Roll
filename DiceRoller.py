import random

def diceroll():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice... ")
    print("🎲 The number you rolled is:", diceroll())
    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break