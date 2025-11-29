import random

while True:
    dice_roll=input("Roll a dice? y/n: ").lower()

    if dice_roll == "y":
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(f"({a},{b})")
    elif dice_roll == "n":
        print("Thanks for playing!")
        break
    else:
        print("Thats an invalid choice!")
        