# picks a random number. You guess until you get it right, with hints along the way!
import random

def main():
    number = random.randint(1, 99)
    print("I'm thinking of a number between 1 and 99...")

    guess = int(input("Enter a guess: "))
    while guess != number:
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Try again: "))

    print("Congrats! The number was:", number)

if __name__ == '__main__':
    main()
