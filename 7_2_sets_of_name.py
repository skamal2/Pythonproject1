names = set()
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
            print(i)
        break