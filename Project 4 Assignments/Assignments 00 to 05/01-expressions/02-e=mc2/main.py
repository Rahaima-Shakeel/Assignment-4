# Calculates and prints the energy equivalent of a given mass using Einstein's mass-energy equivalence formula.
def main():
    C = 299792458  # speed of light in m/s
    mass = float(input("Enter kilos of mass: "))
    energy = mass * C**2
    print(f"e = m * C^2...\nm = {mass} kg\nC = {C} m/s\n{energy} joules of energy!")

if __name__ == '__main__':
    main()