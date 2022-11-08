"""Write a program that asks the user to enter numbers until they input an empty string to quit.
At the end, the program prints out the five greatest numbers sorted in descending order.
 Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument."""

import random
list=[]
users=int(input("Enter number: "))

while users!="":
    users = int(input("Enter number: "))
    list.sort(reverse=users)
    for users in list(0,4):
        print(users)