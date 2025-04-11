# simulates rolling two dice, prints the results of each roll, and displays their total.
import random 

dice_num = 6

def main():
    dice1 : int = random.randint(1,dice_num)
    dice2 : int = random.randint(1,dice_num)

    total : int = dice1 + dice2


    print("Dice have", dice_num, "sides each.")
    print("First die:", dice1)
    print("Second die:", dice2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()