
user = float(input("Give volume in gallons: \n"))
def main():

    result = user * 3.785411784
    return result

while user>-1:

    print(f"{main():.2f} litres.")
    user = float(input("Give volume in gallons: \n"))

