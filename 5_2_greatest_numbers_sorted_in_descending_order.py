users = []
user = input("Enter a number at least 5 times: \n")
while user != "" :
    users.append(user)
    users.sort(reverse = True)

    user = input("Enter a number at least 5 times: \n")
print(users)