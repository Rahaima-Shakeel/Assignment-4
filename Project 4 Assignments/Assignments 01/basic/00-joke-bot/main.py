# Asks the user for input, and if they type "joke" (in any case), it shows a joke—otherwise, it says it only tells jokes.
PROMPT = "What do you want?"
JOKE =  (
    "Here is a joke for you!\n\n"
    "Sophia is heading out to the grocery store.\n"
    "A programmer tells her: \"Get a liter of milk, and if they have eggs, get 12.\"\n"
    "Sophia returns with 13 liters of milk.\n"
    "The programmer asks: \"Why did you get 13?\"\n"
    "Sophia replies: \"Because they had eggs.\"\n"
)
SORRY = "\nSorry I only tell jokes\n"

def main():
    user_input = input(PROMPT).strip().lower()
    
    if  user_input == "joke":
        print("\n" + JOKE)
    else:
        print(SORRY)
        
if __name__ == '__main__':
    main()