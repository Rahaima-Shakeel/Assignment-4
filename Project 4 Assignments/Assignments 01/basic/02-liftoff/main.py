# Uses a for loop to countdown from 10 to 1, with a 0.5 second delay between each number, and then prints "Liftoff!" at the end.
import time
def main():
    # Countdown from 10 to 1
    for i in range(10,0,-1):
        print(i)
        time.sleep(0.5) # delay of 0.5 sec 
    print("Liftoff!")
# This line runs the main function
if __name__ == "__main__":
    main()