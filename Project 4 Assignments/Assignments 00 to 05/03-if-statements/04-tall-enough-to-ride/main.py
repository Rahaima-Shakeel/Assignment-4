# asks for the user's height, checks if it's greater than or equal to the minimum height, and prints a message accordingly.
def main():
    MINIMUM_HEIGHT = 50  
    height = float(input("How tall are you? "))  

    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()