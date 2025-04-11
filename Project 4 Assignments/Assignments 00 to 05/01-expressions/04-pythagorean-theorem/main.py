# prompts the user for the lengths of two sides of a right triangle and calculates the hypotenuse using the Pythagorean theorem.
import math

def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    bc = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is: {bc}")

if __name__ == '__main__':
    main()