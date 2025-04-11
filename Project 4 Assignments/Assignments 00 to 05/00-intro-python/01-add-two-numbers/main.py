# This code defines a main() function that takes two integer inputs from the user, calculates their sum, and prints the result when the script is run directly.
def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    total = num1 + num2
    print(f"The total is {total}.")
if __name__ == '__main__':
        main()