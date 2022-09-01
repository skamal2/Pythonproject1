for _ in range(5):
        username = input("Enter a user name! \n")
        password = input("Enter a password! \n")
        if username=="python" and password=="rules":
            print("Welcome \U0001f600 ")
            break
        else:
                print("Incorrect username or password. \n")
else:
    print("Access denied")


