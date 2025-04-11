# Prints all numbers from 1 to num that divide num with no remainder.
def print_divisors(num):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
