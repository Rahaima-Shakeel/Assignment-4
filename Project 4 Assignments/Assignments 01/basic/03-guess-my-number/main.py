# Generates a secret number between 1 and 100 and asks the user to guess it, providing feedback until the correct number is guessed.
import random

def main():
    secret_number : int = random.randint(1,100)
    print("Think of number between 1 to 100")

    guess = int(input("enter a number:"))

    while guess != secret_number:  # Looping until the user guesses the correct number
        if guess < secret_number:  # Providing feedback on whether the guess is too low or too high
         print("your guess is too low")

        else:
         print("your guess is too high")

        print()# Adding a line break for better readability
        guess = int(input("enter a number:"))

    print(f"congrats your guess number is :" + str(secret_number))

main()