# generates and prints 10 random numbers between 1 and 100 using the random.randint() function in a loop.
import random

def main():
    for _ in range(10):
        print(random.randint(1, 100))

if __name__ == '__main__':
    main()