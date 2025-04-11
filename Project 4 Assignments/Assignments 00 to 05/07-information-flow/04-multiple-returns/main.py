# asks the user for their first name, last name, and email address, then returns and displays these values as a tuple.
def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address: str = input("What is your email address?: ")
    
    return first_name, last_name, email_address

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()