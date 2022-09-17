attempts=0

while attempts<5:
    username= input("Enter a user name:")
    password= input("Enter a Password:")
    attempts+=1

    if username=="python" and password =="rules":
        print("Welcome!")
        break
    if attempts==5 and username=="python" and password =="rules":
        print("Username or password wrong!")
        break
else:
    print("Access Denied!")


#for _ in range(5):
        #username = input("Enter a user name! \n")
        #password = input("Enter a password! \n")
        #if username=="python" and password=="rules":
            #print("Welcome \U0001f600 ")
            #break
        #else:
                #print("Incorrect username or password. \n")
#else:
    #print("Access denied")



