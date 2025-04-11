#  checks if a user is eligible to vote in three fictional countries based on their age and prints the result for each country.
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

user_age = int(input("Enter your Age: "))

if user_age >= PETURKSBOUIPO_AGE:
    print("You can vote in Peturksbouipo ✅")
else:
    print(f"You can't vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE} ❎")

if user_age >= STANLAU_AGE:
    print("You can vote in Stanlau ✅")
else:
    print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE} ❎")

if user_age >= MAYENGUA_AGE:
    print("You can vote in Mayengua ✅")
else:
    print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE} ❎")