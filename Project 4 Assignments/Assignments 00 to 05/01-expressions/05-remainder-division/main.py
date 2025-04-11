# Asks for two numbers and directly prints the result of the division and remainder.
def main():
    a = int(input("Enter an integer to be divided: "))
    b = int(input("Enter an integer to divide by: "))
    print("The result of this division is", a // b, "with a remainder of", a % b)

if __name__ == '__main__':
    main()
