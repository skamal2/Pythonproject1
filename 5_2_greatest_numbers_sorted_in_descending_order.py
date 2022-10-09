import random
users=int(input("Enter number: "))

while users!=29:
    if users >= 1 and users <= 3:
        print("prime")
    users = int(input("Enter number: "))
    r=random.randint(2,10)
while users!=users and users%r==0:
    print("composite")