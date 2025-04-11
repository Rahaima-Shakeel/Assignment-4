# The Planetary Weight Calculator allows users to input their Earth weight and select a planet to calculate and display their equivalent weight on that planet based on its gravity multiplier.
GRAVITY_MULTIPLIERS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    # Get weight input from the user
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Get planet input from the user
    planet = input("Enter a planet: ").capitalize()

    # Check if the planet is valid and calculate weight on the planet
    if planet in GRAVITY_MULTIPLIERS:
        planetary_weight = round(earth_weight * GRAVITY_MULTIPLIERS[planet], 2) #multiplies the Earth weight by the gravity multiplier and rounds the result to two decimal
        print(f"The equivalent weight on {planet}: {planetary_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()
