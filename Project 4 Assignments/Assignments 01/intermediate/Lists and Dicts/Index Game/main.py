# The Index Game allows users to interact with a list by accessing, modifying, or slicing elements, handling invalid inputs.
def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    
    
# Access: Get the value of an item at a specific position in the list.
# Modify: Change an item at a specific position.
# Slice: Extract a part of the list using start and end positions.
    operation = input("Choose an operation (access/modify/slice): ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        if 0 <= index < len(lst):
            print(lst[index])
        else:
            print("Index out of range.")
    
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        if 0 <= index < len(lst):
            new_value = input("Enter new value: ")
            lst[index] = new_value
            print("Updated list:", lst)
        else:
            print("Index out of range.")
    
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        if 0 <= start < len(lst) and 0 <= end <= len(lst):
            print(lst[start:end])
        else:
            print("Invalid indices.")
    
    else:
        print("Invalid operation.")

index_game()
