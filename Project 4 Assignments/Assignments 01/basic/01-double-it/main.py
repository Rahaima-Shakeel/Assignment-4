# Asks the user to enter a number. It keeps doubling the number and printing the result until the number becomes 100 or greater.
def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
     # Keep doubling the number until it is 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2 # Double the value
        print(curr_value) # Print the new value
# # Python file to call the main() function.
if __name__ == '__main__':
    main()