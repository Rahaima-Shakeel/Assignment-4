# keeps asking the user for values and adds them to a list until the user presses Enter without typing anything. Then, it prints the list.
def get_list():
    
   lst = []
   while True:
       element = (input("Enter the elements you wanna create list of: "))
       if element == "":
           break
       lst.append(element)
   print("Here's the list of your elements",lst)

get_list()