"""Write a program that asks the user to enter numbers until they input an empty string to quit.
At the end, the program prints out the five greatest numbers sorted in descending order.
 Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument."""


list=[]
while True:
    users = input("Enter number: ")
    if users =="":
        break
    list.append(int(users))
    list.sort(reverse=True)

for i in (list[0:5]):
    print(i)
