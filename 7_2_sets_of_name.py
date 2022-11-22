"""Write a program that asks the user to enter names until he/she enters an empty string.
After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
Finally, the program lists out the input names one by one, one below another in any order.
 Use the set data structure to store the names."""

names = {"ram", "sam", "bam", "pam"}
while True:
    name= input("Enter the name: ")

    if name !="":
        if name not in names:
            print ("New name. ")
        elif name in names:
            print("Existing name. ")
        names.add(name)
    else:
        print(f"The names are:")
        for i in names:
            print([i])
        break
"""names = {"ram", "sam", "bam", "pam"}
user=input("Enter names: ")
while user != "":

    if user in names:
        names.add(user)
        print("exists")
    if user not in names:
        print("New name. ")
        names.add(user)
    user = input("Enter names: ")

for i in names:
    print(i)
"""