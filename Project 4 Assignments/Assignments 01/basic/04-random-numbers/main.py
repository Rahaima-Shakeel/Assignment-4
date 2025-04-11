# Uses a `for` loop with `range(10)` to print 10 random numbers between 1 and 100 using `random.randint()`.
import random

N_NUMBERS: int = 10 # Total number of random numbers to generate
MIN_VALUE: int = 1 # Minimum value 
MAX_VALUE: int = 100 # Maximum value 

def main():
    for i in range(N_NUMBERS):
     print(random.randint(MIN_VALUE,MAX_VALUE))

if __name__ == '__main__':
    main()