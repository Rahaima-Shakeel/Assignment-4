# The user to enter a temperature in Fahrenheit and converts it to Celsius, then displays both temperatures.
def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature: {fahrenheit} F = {celsius} C")

if __name__ == '__main__':
    main()