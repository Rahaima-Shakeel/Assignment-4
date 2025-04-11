# prompts the user to input a specified number of elements into a list and prints the last element of the list.
def get_last_element(lst):
    print(lst[-1])

lst = []
n = int(input("How many elements in the list? "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

get_last_element(lst)