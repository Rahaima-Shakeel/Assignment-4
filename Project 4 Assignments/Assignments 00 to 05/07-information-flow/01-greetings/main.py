# Takes the user's name and prints a friendly greeting using a helper function.
def greet(name):
    return "Greetings " + name + "!"

def main():
    name = input("What's your name? ")
    print(greet(name))

if __name__ == '__main__':
    main()