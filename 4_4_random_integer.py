import random
user = int(input("Guess the number: "))
random_integer = random.randint(1,10)
while user!= random_integer:
    if user > random_integer:
        print("Your number is too high!")
    if user < random_integer:
        print("Your number is too low!")
    user = int(input("Guess the number: "))
print("Congratulations! Correct number is " + str(random_integer))

#2nd procedure
#user = int(input("Guess the number:"))
#random_integer = random.randint(1,10)
#while user> random_integer:
        #print("Your number is too high!")
       # user = int(input("Guess the number:"))
#while user < random_integer:
        #print("Your number is too low!")
        #user = int(input("Guess the number:"))
#print("Congratulations! Correct number is " + str(random_integer))