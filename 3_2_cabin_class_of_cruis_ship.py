customer = input("Enter the cabin class of a cruise ship(only upper characters) \n")
if customer == ("LUX"):
    print("Upper-deck cabin with a balcony. \n")
elif customer =="A":
    print("Above the car deck, equipped with a window. \n")
elif customer =="B":
    print("Windowless cabin above the car deck. \n")
elif customer == "C":
    print("Windowless cabin below the car deck. \n")
else:
    print("Invalid cabin class.")