# rolling two dice three times, printing the result of each roll with the values of the two dice displayed
import random 

dice_num = 6

def main():
    dice1 : int = random.randint(1,dice_num)
    dice2 : int = random.randint(1,dice_num)

    print(f"rolled: {dice1}  {dice2}")

print("Rolling two dice three times:")
for dice in range(3):
        main()