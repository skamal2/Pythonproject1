
import requests
def connectDatabase():
    import mysql.connector
    myDb = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_simulator',
            user='skamal',
            password='Villain',
            autocommit=True
        )
    return myDb.cursor()

class reachedDestination:
    def __init__(self, player, distance, move):
        self.pName = player
        self.aDist = distance
        self.pMove = move

    def calculatePoints(self):
        return round(self.aDist / self.pMove, 2)

    def updateNewPoints(self):
        # connect to database
        import mysql.connector
        myDb = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_simulator',
            user='skamal',
            password='Villain',
            autocommit=True
        )
        myCursor = myDb.cursor()
        pPoints = self.calculatePoints()
        myCursor.execute(f"insert into users(name, distance, moves, points) values('{self.pName}',{self.aDist},{self.pMove},{pPoints});")


'''
x = reachedDestination('mong', 10, 9)
x.calculatePoints()
x.updateNewPoints()
You sent
import random
def generateNumber(num):
    return random.randint(1, num)
You sent
def helpMenu():
    from tabulate import tabulate
    print("\nHOW TO PLAY")
    print(tabulate([["* Step 1: You have to input your name"],
        ["* Step 2: Select destination airport by entering a number in Distance(km) column"],
        ["* Step 3:"],
        ["    - System then generates a random number to let you guess"],
        ["    - Then try to input a number in range of 1 <= input <= distance)"],
        ["    - Every time you entered a number, it counts 1 move"],
        ["    - Turn left: you must input a number that smaller than the previous one"],
        ["    - Turn right: you must input a number that greater than the previous one"],
        ["    - Repeat until you guessed the right number, means you have landed"],
        ["    - After that you will see your points (distance / moves) and the top 5 players"],
        ["    - The longer the distance, the more points you get"]], tablefmt="double_outline"))
You sent
"""
This module is main file of the program. It combines other modules to have a full game
"""
# Import module files
from help import *
from top5Players import *
from showDestTable import *
from generateNum import *
from gameEnd import *
from resetPoint import *
#from connectDb import *
from tabulate import tabulate

# Show menu of the first screen
print("\nWelcome to the FLIGHT GAME")
print("Select an option:")
print(tabulate([["1: Help"], ["2: Play"],["3: Top 5 Players"], ["4: Reset points"], ["Enter: quit game"]], tablefmt="double_outline"))
userChoice = input("Your selection: ")
while userChoice == "1" or userChoice == "2" or userChoice == "3" or userChoice == "4":
    if userChoice == "1": #show help menu
        helpMenu()
    elif userChoice == "2": #start to play game
        # get player's name
        playerName = input("What is your name? ")
        # display all destination airport to let player chooses one
        showDestinationTable()
        # ask to select destination
        destAirport = int(input("Select an airport by its number from the above table: "))
        # generate a random number from selected airport
        flightNumber = str(generateNumber(destAirport))
        #print("flight number is: ", flightNumber)
        # Flying: loop until the player input the same flight number
        print("Taking off...")
        playerTry = input("Flying: ")
        moves = 1
        print(tabulate([[f"Your moves: {moves}"]], tablefmt="outline"))
        while playerTry != flightNumber:
            # compare the last input number to flightNumber to give player a suggestion
            if int(playerTry) < int(flightNumber):
                playerTry = input("Turn right: ")
            else:
                playerTry = input("Turn left: ")
            moves += 1
            print(tabulate([[f"Your moves: {moves}"]], tablefmt="outline"))

        print("Landed")
        print(tabulate([[f"Your moves: {moves}"]], tablefmt="outline"))
        # update player's name and new score to users table
        flightInfo = reachedDestination(playerName, destAirport, moves)
        finalPoints = flightInfo.calculatePoints()
        flightInfo.updateNewPoints()

        # Show player's score
        print("Well done", playerName, ", you got", finalPoints, "points")

        # show top 5 players
        top5Players()

    elif userChoice == "3": #show top 5 players from database
        top5Players()

    elif userChoice == "4": #Reset users table to default values
        resetPlayerPoints()

    print("Select an option:")
    print(tabulate([["1: Help"], ["2: Play"], ["3: Top 5 Players"], ["4: Reset points"], ["Enter: quit game"]], tablefmt="double_outline"))
    userChoice = input("Your selection: ")
You sent
def resetPlayerPoints():
    print("Resetting...")
    # connect to database
    import mysql.connector
    myDb = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_simulator',
        user='skamal',
        password='Villain',
        autocommit=True
    )
    myCursor = myDb.cursor()
    myCursor.execute("drop table if exists users;")
    myCursor.execute("create table users(name varchar(10),distance int,moves int,points float);")
    myCursor.execute("insert into users(name, distance, moves, points)values('A', 10, 6, 1.67),"
                     "('B', 10, 7, 1.43),('C', 10, 8, 1.25),('D', 10, 9, 1.11),('E', 10, 10, 1);")
    print("Player table has been reset to the default values \n")
You sent
def showDestinationTable():
    from tabulate import tabulate
    # connect to database
    import mysql.connector
    myDb = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_simulator',
        user='skamal',
        password='Villain',
        autocommit=True
    )
    myCursor = myDb.cursor()
    myCursor.execute("select row_number() over(order by airport.name) + 9, airport.name, "
                     "country.name from airport, country where airport.iso_country = country.iso_country "
                     "and country.name = 'Finland' and (airport.type = 'medium_airport' or airport.type = 'large_airport');")
    result = myCursor.fetchall()
    print(tabulate(result, headers=["Distance(km)", "Airport Name", "Country"], tablefmt="double_outline"))
You sent
def top5Players():
    from tabulate import tabulate
    # connect to database
    import mysql.connector
    myDb = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_simulator',
        user='skamal',
        password='Villain',
        autocommit=True
    )
    myCursor = myDb.cursor()
    myCursor.execute("select row_number() over(order by points desc),name,distance,moves,points from users limit 5;")
    result = myCursor.fetchall()
    print("\nTop 5 players:")
    print(tabulate(result, headers=["Rank", "Name", "Distance(km)", "Moves", "Points"], tablefmt="double_outline"))
    '''

