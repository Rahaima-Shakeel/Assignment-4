# prints whether numbers from 10 to 19 are even or odd.
def main():
    for i in range(10, 20):
        if i % 2 == 0:
            print(f"{i} even")
        else:
            print(f"{i} odd")

if __name__ == '__main__':
    main()