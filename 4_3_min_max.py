user = input("Enter a number: ")
maxnum = user
minnum = user
while user!="":
    if(user > maxnum):
        maxnum = user

    if(user < minnum):
        minnum = user
    user = input("Enter a number: ")
print("The smallest number is: " + (minnum))
print("The largest number is: " + (maxnum))