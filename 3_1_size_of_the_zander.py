zander = float(input("What´s the length of a zander in centimeters? \n"))
if zander < 42:
    short_by=float(42-zander)
    print(f"The size of a zander is short by {short_by:.2f}")
    print("Release the fish!")