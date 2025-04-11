# Checks if a person's age is 18 or older and returns True for adults, False otherwise.
ADULT_AGE = 18  

def is_adult(age: int):
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == '__main__':
    main()