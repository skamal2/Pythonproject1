user = int(input("Enter a number: \n"))
if (user>0 and user<=3):
    print("It´s a prime number.")
if user > 3:
    for i in range(2,user):
        if user%i==0:
            print("It´s not a prime number.")
            break
    else:
        print("It´s a prime number.")

