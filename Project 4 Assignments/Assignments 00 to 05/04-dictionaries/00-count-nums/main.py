#  allows the user to input numbers, counts the occurrences using a dictionary, and prints the results when the user enters a blank line.
def main():
    num_dict = {}
    
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        num_dict[num] = num_dict.get(num, 0) + 1
    
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

if __name__ == '__main__':
    main()