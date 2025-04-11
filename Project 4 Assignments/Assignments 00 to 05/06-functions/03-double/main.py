# defines a double() function that multiplies a number by 2, then prompts the user to input a number and prints its double.
def double(num):
     return num * 2

def main():
        num = int(input("Enter a number: "))
        print(f"Double that is {double(num)}")

main()