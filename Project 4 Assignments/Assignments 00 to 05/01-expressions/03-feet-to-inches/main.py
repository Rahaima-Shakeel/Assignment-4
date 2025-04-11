# takes the number of feet from the user, converts it to inches, and prints the result.
def main():
    feet = float(input("Enter number of feet: "))
    print(f"That is {feet * 12} inches!")

if __name__ == '__main__':
    main()