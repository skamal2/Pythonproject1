#!/usr/bin/python3

for _ in range(3):
        usr = input("Enter username: ")
        psw = input("Enter password: ")

        if usr == "bank_admin" and psw == "Hytu76E":
                print("Access Granted!")
                break
        else:
                print("Access Denied!")
        print("Try Again!")
else:
        print("No more attemps!")

        username = input("Enter a user name! \n")
        password = input("Enter a password! \n")
        while username == "python" and password == "rules":
                print("Welcome \U0001f600 ")
                break
        i = 0
        while i < 5:
                print("Incorrect username or password. \n""Try again!")
                username = input("Enter a user name! \n")
                password = input("Enter a password! \n")
                i = i + 1
                print("access denied")
                break


