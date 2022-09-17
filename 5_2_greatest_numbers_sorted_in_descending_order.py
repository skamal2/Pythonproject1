users = []
user=0
while user != "" :
    user =(input("Enter a number at least 5 times: \n"))
    if user != "":
        user = int(user)
        users.append(int(user))

        users.sort(reverse = True)


print(users)
print("The greatest numbers are: ", users[0:6])