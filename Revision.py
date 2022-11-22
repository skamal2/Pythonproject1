
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
##20
"""
user=int(input("How many items to be added? \n"))
list=[]
i=1
while user>0:
    ask=int(input(f"Item {i}: "))
    list.append(ask)
    user=user-1
    i=i+1
print(list)"""

##21
"""Removing items from a list
There are two different approaches to removing an item from a list:

If the index of the item is known, you can use the method pop.
If the contents of the item are known, you can use the method remove.
So, the method pop takes the index of the item you want to remove as its argument. 
The following program removes items at indexes 2 and 3 from the list.
 Notice how the indexes of the remaining items change when one is removed."""

"""
my_list = [1, 2, 3, 4, 5, 6]

my_list.pop(2)
print(my_list)
my_list.pop(3)
print(my_list)"""
##22
"""Please write a program which asks the user to choose between addition and removal. 
Depending on the choice, the program adds an item to or removes an item from the end of a list. 
The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
The list is printed out in the beginning and after each operation. Have a look at the example execution below:"""
"""my_list = []
i=1
while True:
    user = input("What do you want? \n")
    if user=="x":
        print("Thanks!Bye!")
        break
    if user == "a":
        my_list.append(i)
        print(f"The list now is {my_list}")
        i = i + 1
    if user == "r":
        my_list.pop((len(my_list))-1)
        print(f"The list now is {my_list}")"""

##23
"""
Please write a program which asks the user for words.
 If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

Sample output
Word: once
Word: upon
Word: a
Word: time
Word: upon
You typed in 4 different words"""
"""
my_list = []
while True:
    user = input("Enter words: ")
    if user in my_list:
        print(f"The number of different words are {len(my_list)}")
        break
    my_list.append(user)"""

#my_list = [2,5,1,2,4]###Sorted function can be very handy
#print(sorted(my_list))

##24 Please write a program which asks the user to type in values and adds them to a list.
# After each addition, the list is printed out in two different ways:
# in the order the items were added ordered from smallest to greatestThe program exits when the user types in 0.
# An example of expected behaviour:
"""
my_list=[]

while True:
    user=int(input("Enter numbers: "))
    if user==0:
        print("Bye!")
        break
    if user != 0:
        my_list.append(user)
        print(f"The list now is {my_list}")
        print(f"The sorted list is {sorted(my_list)}")"""

##26
"""
my_list = [5, 2, 3, 1, 4]
greatest = max(my_list)
smallest = min(my_list)
list_sum = sum(my_list)
print("Smallest:", smallest)
print("Greatest:", greatest)
print("Sum:", list_sum)"""

##27 Airthemetic mean
"""
my_list = [1, 2, 3, 4, 5]
sum= sum(my_list)
length=len(my_list)
result = sum/length
print("mean value is", int(result))"""

##28The for loop
# When you want to go through some ready collection of items, the Python for loop will do this for you. For instance,
# the loop can go through all items in a list from first to last.
# When using a while loop the program doesn't "know" beforehand how many iterations the loop will perform.
# It will repeat until the condition becomes false, or the loop is otherwise broken out of. That is why it falls under indefinite iteration.
# With a for loop the number of iterations is determined when the loop is set up, and so it falls under definite iteration.
# The idea is that the for loop takes the items in the collection one by one and performs the same actions on each.
# The programmer does not have to worry about which item is being handled when. The syntax of the for loop is as follows:

#for <variable> in <collection>:
    #<block>

##29 Star Studded
#Please write a program which asks the user to type in a string.
# The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.


"""user=input("Write a word: ")

for i in user:
    print(i)
    print("*")"""

##30
#The function range
#Often you know how many times you want to repeat a certain bit of code.
# You might, for example, wish to go through all the numbers between 1 and 100.
# The range function plugged into a for loop will do this for you.
#There are a few different ways to call the range function.
# The simplest way is to give the function just one argument, which signifies the end-point of the range.
# The end-point itself is excluded, just like with string slices. In other words, the function call range(n)
# provides a loop with a range from 0 to n-1:

"""for i in range(5):
    print(i)
    print("**")"""
"""for i in range(1, 9, 2):
    print(i)"""
"""for i in range(6, 2, -1):
    print(i)"""

"""Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, 
but leaves out the number 0. Each number should be printed on a separate line."""
"""user = int(input("Enter number: "))
neg=-(user)
for i in range((neg),user+1):
    print(i)"""
##30 Please write a function named list_of_stars, which takes a list of integers as its argument.
# The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.
#For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:
"""***
*******
*
*
**"""


"""def list_of_stars(lis):
    lis=[]
    for i in range(lis):
        print(i)
        
        return (lis)
m=[2,3,4,5]
list_of_stars(m)"""

##31
#Please write a function named anagrams, which takes two strings as arguments.
#The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.

"""def anagrams(a,b):

    if sorted(a)==sorted(b):
        print("True")

    else:
        print("False")
    return
anagrams("car","rc")"""


##32 sum of positive numbers

"""def sumed(numbers):
    m = 0
    for i in numbers:

        if i>0:
            m=m+i
            return m

list=[1,-3,2,-4,5]
a= sumed(list)
print(a)"""


"""my_list = ["Hi", "there", "example", "one more"]

for i in my_list:
    my_list.reverse()
    print(i)"""
"""my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["apina"])

word = input("Please type in a word: ")
if word in my_dictionary:
    print("Translation: ", my_dictionary[word])
else:
    print("Word not found")"""

"""Please write a function named times_ten(start_index: int, end_index: int),
which creates and returns a new dictionary. The keys of the dictionary should be the numbers between 
start_index and end_index inclusive
The value mapped to each key should be the key times ten."""

"""def times_ten(start_index: int, end_index: int):
    for key, value in times_ten.items():
        value=key*10

        return key, value
a=times_ten(3, 6)
print(a)"""
"""my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for a in my_dictionary:
    print("key:", a)
    print("value:", my_dictionary[a])
for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)"""

"""word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]
def counts(word_list):
    words = {}
    for word in word_list:
        # if the word is not yet in the dictionary, initialize the value to zero
        if word not in words:
            words[word] = 0
        # increment the value
        words[word] += 1
    return words


# call the function
print(counts(word_list))"""

"""Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. 
The keys of the dictionary should be the numbers between start_index and end_index inclusive
The value mapped to each key should be the key times ten."""

"""times_ten={3, 6}
for key, value in times_ten.items():
    print(key, value*10)"""
###Error handling
"""try:
    age = int(input("Please type in your age: "))
except ValueError:
    age = -1
if age >= 0 and age <= 150:
    print("That is a fine age")
else:
    print("This is not a valid age")"""

"""def read_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            return int(input_str)
        except ValueError:
            print("This input is invalid")

number = read_integer()
print("Thank you!")
print(number, "to the power of three is", number**3)"""


"""def read_integer():
    try:
        input_str = input("Please type in an integer: ")
        return int(input_str)
    except ValueError:
        print("This input is invalid")


number = read_integer()
print("Thank you!")
try:
    print(number, "to the power of three is", number ** 3)
except TypeError:
    print("dfghfds")"""

"""def read_small_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            number = int(input_str)
            if number < 100:
                return number
        except ValueError:
            pass # this command doesn't actually do anything

        print("This input is invalid")

number = read_small_integer()
print(number, "to the power of three is", number**3)"""

"""class BankAccount:

    # The constructor
    def __init__(self, balance: float, owner: str):
        self.balanc = balance
        self.owne = owner

# As the method is called, no argument should be given for the self parameter
# Python assigns the value for self automatically
peters_account = BankAccount(100, "Peter Python")
paulas_account = BankAccount(20000, "Paula Pythons")

print(peters_account.balanc)
print(paulas_account.balanc)"""

"""Please write a class named Book with the attributes name, author, genre and year, along with 
a constructor which assigns initial values to these attributes.
Your class should work like this:
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")"""

"""class Book:
    def __init__(self,bookname: str, author: str, genre: str, year: int):
        self.bookname = bookname
        self.author = author
        self.genre = genre
        self.year = year

python = Book( "Fluent Python" , "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
print(f"{python.author}: {python.bookname} ({python.genre})")
print(f"The genre of the book {everest.bookname} is {everest.genre}")"""

"""Please define the class Pet. The class should include a constructor, which takes the initial values of the attributes name, species and
year_of_birth as its arguments, in that specific order.Please also write a function named new_pet(name: str, species: str, year_of_birth: int) 
outside the class definition. The function should create and return a new object of type Pet, as defined in the class Pet.
An example of how the function is used:

fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)
Sample output
Fluffy
dog
2017"""

"""class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name=name
        self.species=species
        self.year_of_birth=year_of_birth

    def new_pet(name: str, species: str, year_of_birth: int):

        fluffy=Pet("Fluffy", "Pomerian", 2017)
        return fluffy

Fluffy=fluffy.new_pet


print(Fluffy.name)
print(Fluffy.species)
print(Fluffy.year_of_birth)"""

"""class Car:
    def __init__(self, plate_number, colour):
        self.plate_number = plate_number
        self.colour = colour

class PaintShop:
    pass
    def paint(self, car, colour):
        car.colour = colour

paint_shop = PaintShop()
car = Car("ABC-123", "blue")
print("The car is " + car.colour)
paint_shop.paint(car, "red")
print("The car is now " + car.colour)"""

class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor
        return
    def go_up(self,up_floor):

        for i in range(self.current_floor,up_floor):
            self.current_floor = self.current_floor+i
            print(f"Going floor {i} to {i+1}")
        m=up_floor
        while m !=1:
            print(f"Going floor {m} to {m-1}")
            m=m-1

        return True
    def go_down(self, down_floor):
        for i in range(self.current_floor, down_floor,-1):
            self.current_floor = self.current_floor-i
            print(f"Going floor {i} to {i-1}")

        n = down_floor
        while n != 1:
            print(f"Going floor {n} to {n - 1}")
            n = n - 1

        return True
    def go_to_floor(self, floor):
        if floor > self.current_floor:
            self.go_up(floor)
            return True
        if floor < self.current_floor:
            self.go_down(floor)
            return True
        if floor == self.current_floor:
            print(f"You are in {self.current_floor} floor now.")
            self.go_down(floor)

            return True
class Building:
    def __init__(self, list_of_elevators:list):
        self.list_of_elevators = []
        for i in range(list_of_elevators):
            self.list_of_elevators.append(elevator)

    def run_elevator(self,no_of_elevators, floor):
        print(f"The elevator number {no_of_elevators} is running")
        self.list_of_elevators[no_of_elevators - 1].go_to_floor(floor)


elevator = Elevator(1,9,5)
elevator = Elevator(1,9,3)
elevator = Elevator(1,9,7)
building = Building(3)
target_floor = int(input("Which floor would you like to go to? \n"))

elevator.go_to_floor(target_floor)

print("Elevator in the building.")
building = Building(1, 7, 3)
building.run_elevator(1, 4)
building.run_elevator(2, 5)
building.run_elevator(3, 2)