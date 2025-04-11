# Prompts the user for a number, calculates its square, and prints the result
def main():
    num = float(input("Enter a number to see its square: "))
    print(f"{num} squared is {num ** 2}")
    
if __name__ == '__main__':
    main()