gender = input("Give gender: \n").lower()
hmb= float(input("Hmb level: \n"))
if (gender == "male") and (hmb >167):
    print("Your hmb is high")
elif((gender == "female") and (hmb >155)):
    print("Your hmb is high")
elif(gender == "male") and (hmb <134):
    print("Your hmb is low")
elif((gender == "female") and (hmb <117)):
    print("Your hmb is low")
else:
    print("normal")