"""year = int(input("Give year:"))

leap = (year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0)

original = year+1
while original!=leap:
    original += 1


print(f"The next leap year from {original} is {year}")"""

#2

"""Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in zero.
After reading in the numbers the program should print out how many numbers were typed in. 
The zero at the end should not be included in the count.

You will need a new variable here to keep track of the numbers typed in.
The program should also print out the sum of all the numbers typed in. 
The zero at the end should not be included in the calculation. Find mean number of positive and negative numbers.

user=int(input("Give: "))
i=0
sum=0
positive=0
n = 0
while user !=0:
    if user > 0:
        positive = positive + 1


    if user < 0:
        n = n + 1

    sum = sum + user
    user = int(input("Give: "))
    i=i+1
    m=0


print(i)
print(sum)

print(f"mean: {sum/i}")
print(f"positive: {positive}")
print(f"negative: {n}")
"""

#3
"""Please write a program which prints out all the even numbers between two and thirty, using a loop.
 Print each number on a separate line."""
""""
number = 2
while number<32:

    print(number)
    number = number + 2"""

#4
"""Fix the countdown
print("Are you ready?")
number = int(input("Please type in a number: "))
while number != 0:

    print(number)
    number = number - 1
print("Now!") """

#5
"""sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    if number >= 10:  # The property of continue is that when the given 
    condition is met the loop will ignore taking account of that input. 
    Everything will be ignored after continue and the loop will be started again. 
    Differences between break and continue 
    is after break loop is ended but after continue condition is met loop will be continued again from the begining.
        continue
    sum += number

print (f"The sum is {sum}")"""

#6
"""Multiplication table from 1 to 5

num=0
while num<5:
    num=num+1
    number=1
    while number<6:

        print(f"{num} times {number}={num*number}")
        number = number + 1
        """

#7
""""Please write a program which asks the user to type in a sentence. 
The program then prints out the first letter of each word in the sentence, each letter on a separate line."""


#8
""""Factorial"""
"""
while True:
    user = int(input("Give number: "))
    if user <= 0:
        print("Thanks!Bye!")
        break


    product=1
    while user>0:
        product=product*user
        user=user-1


    print(product)"""

#9
#First letter of user input
"""user=input("Give words: ")
x=user.split(" ")
m=user[0][0]
print(m)
"""

##Functions: The Python built-in functions are defined as the functions whose functionality is pre-defined in Python.
# The python interpreter has several functions that are always present for use.
# These functions are known as Built-in Functions.e.g bool(), abs()

"""
def message():
    print("This is my very own function!")

message()
message()
message()"""
##mean
#Please write a function named mean, which takes three integer arguments.
#The function should print out the arithmetic mean of the three arguments.
"""def mean(x,y,z):
    result=(x+y+z)/3
    print(f"The airthmetic mean of {x}, {y}, {z} is {result}.")
mean(7,3,5)

"""
##10 how many times??

"""
def many_times(text, times):
    i=0
    while i <times:
        print(text)
        i=i+1

text = "All Pythons, except one, grow up"
times = 3
many_times("ram", 4)"""

##11 Square of hashes

"""def square(size):
    i=0
    while i<size:
        print(f"#"*size)##to print horizontally
        i=i+1
square(3)"""

##12 Chessboard

"""def chess(times):
    i=0
    while i<times:
        print(("10")*(times-2))
        i += 1



chess(5)"""

##13 line

"""def line(times,a):
    if a=="":
        print(("*"*times))

    print(a*times)

line(5,"m")
line(4,"%")
line(6,"")"""

##14 A rectangle box of hashes

"""def line(a):
    while a>0:
        print("#"*10)
        a=a-1

line(2)
print()
line(4)"""

##15 square
"""
def height(length,a):
    i=0
    while i<length:
        print(a*length)
        i+=1


height(4,"*")"""

##16triangle
"""
def triangle(line):
    i=1
    while i!=line:
        print("*"*i)
        i=i+1

triangle(5)"""
##17 ShapePlease write a function named shape, which takes four arguments.
# The first two parameters specify a triangle, as above, and the character used to draw it.
# The first parameter also specifies the width of a rectangle, while the third parameter specifies its height.
# The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle,
# and then the rectangle below it.
# The function should call the function line from the exercise
# above for the actual printing out. Copy your solution to that
# exercise above the code for this exercise. Please don't change anything in the line function.
"""
def shape(a,b,c,d):
    i = 0
    while i != a:
        print(b * (i+1))
        i = i + 1
    i = 0
    while i != c:
        print(d*a)
        i = i + 1

shape(5,"X",3,"*")"""

##17 Spruce tree
"""
def spruce(size):
    i=1
    while i<=size:
        print(" *"*i)
        i=i+2

spruce(5)"""

##18 Return values
"""
def ask_for_name():
    name = input("What is your name? ")
    return name

name = ask_for_name()
print("Hello there,", name)"""
"""
my_list = [7, 2, 2, 5, 2]

print(my_list[0])
print(my_list[1])
print(my_list[-3])
print("The sum of the first two items:", my_list[0] + my_list[1])"""

"""Unlike strings, 
lists are mutable, which means their contents can change. 
You can assign a new value to an item within a list, just like you can assign a new value to a variable:

my_list = [7, 2, 2, 5, 2]
print(my_list)
my_list[1] = 3
print(my_list)"""

##19 Please write a program which initialises a list with the values [1, 2, 3, 4, 5].
# Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again.
# This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.
"""
list = [1,2,3,4,5]
index = int(input("Enter index: "))
new_list_number = int(input("Enter index: "))
list[index]=new_list_number
print(list)"""

## 19The append method adds items to the end of a list. It works like this:
"""
numbers = []
numbers.append(5)
numbers.append(10)
numbers.append(3)
print(numbers)"""