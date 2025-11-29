import random
random_number = random.randint(1, 100)

while True:

    number_guess = int(input("Guess the number between 1 and 100: "))
    
    if number_guess == random_number:
        print("Conguratulations! You guessed the number.")
        break
    elif number_guess < random_number:
        print("Too low!")
    elif number_guess > random_number:
        print("Too high!")
    else:
        print("Please enter a valid number.")
