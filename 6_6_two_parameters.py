import math


def main(diameter, price):
    per_unit_square_price = price / ((math.pi) * (diameter / 200) ** 2)

    return per_unit_square_price


print("Value of first pizza: ")
diameter = float(input("Enter the diameter of first pizza in cm: "))
price = float(input("Enter the price of the first pizza: "))
zz=(main(diameter, price))
print(zz)

while (True):

    print("Value of second pizza: ")
    diameter = float(input("Enter the diameter of second pizza in cm: "))
    price = float(input("Enter the price of the second pizza: "))

    print(main(diameter, price))
    if (zz) > (main(diameter, price)):
        print("Value of second pizza is better.")

    elif (zz)<(main(diameter, price)):
        print("Value of first pizza is better.")

    else:
        print("Value of both pizza is same.")

    break