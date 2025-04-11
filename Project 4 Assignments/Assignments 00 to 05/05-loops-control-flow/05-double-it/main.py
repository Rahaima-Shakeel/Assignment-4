# prompts the user to enter a number, then repeatedly doubles the value of that number, printing each result, until the value reaches or exceeds 100.
def main():
    curr_value = int(input("Enter a number: "))
    
    while curr_value < 100:
        print(curr_value)
        curr_value = curr_value * 2
        
    print(curr_value)

if __name__ == '__main__':
    main()