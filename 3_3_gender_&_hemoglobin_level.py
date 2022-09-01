gender = input("Write your biological gender. \n")
gender = gender.lower()
hemoglobin = float(input("Write your hemolglobin level in gram per liter(g\l). \n"))
if gender == "female" and (117<hemoglobin<155) or gender == "male" and (134<hemoglobin<167):
    print("Your hemoglobin level is normal")
elif gender == "female" and (hemoglobin>=155) or gender =="male" and (hemoglobin>=167):
    print("Your hemoglobin level is high")
elif gender == "female" and (hemoglobin<=117) or gender =="male" and (hemoglobin<=134):
    print("Your hemoglobin level is low")