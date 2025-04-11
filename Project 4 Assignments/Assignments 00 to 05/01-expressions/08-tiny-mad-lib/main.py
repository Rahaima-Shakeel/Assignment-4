# A simple Mad Libs game that asks for a color, animal, and action to create a fun sentence.
def main():
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    action = input("Enter an action (verb): ")

    print(f"Once upon a time, a {color} {animal} decided to {action} across the forest, spreading joy everywhere!")

if __name__ == '__main__':
    main()