# defines a helper function subtract_seven to subtract 7 from a number and then calls it in the main() function, printing the result, which should be zero.
def subtract_seven(num):
    num = num - 7
    return num

def main():
    num: int = 7
    num = subtract_seven(num)
    print("This should be zero:", num)

if __name__ == '__main__':
    main()