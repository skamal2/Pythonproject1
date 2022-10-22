import random
import sys
import mysql.connector
from geopy.distance import geodesic as GD
from tabulate import tabulate

import requests

count = 0


def greet():
    print(f"Congratulations! Goal reached! \U0001f600")
    global count
    count += 1

    if count == 8:
        print(f"\033[92m Yay! You won! \U0001f600 \U0001f600 \U0001f600")
        print("Play Again!")

    return


x = count


def fetch_information(name):
    sql = "SELECT  latitude_deg from airport"
    sql += " WHERE name ='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:

        for row in result:
            return (row[0])


def fetch_information1(name):
    sql = "SELECT  longitude_deg from airport"
    sql += " WHERE name ='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return (row[0])


def fetch_information2(ident):
    sql = "SELECT  latitude_deg from airport"
    sql += " WHERE ident ='" + ident + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:

        for row in result:
            return (row[0])


def fetch_information3(ident):
    sql = "SELECT  longitude_deg from airport"
    sql += " WHERE ident ='" + ident + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return (row[0])


def fetch_information4(ident):
    sql = "SELECT Name, Municipality, Ident, Iso_country FROM airport"
    sql += " WHERE ident='" + ident + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:

        for row in result:
            print(f"Current location: The name of the airport is {row[0]} and it is located  in {row[1]}, {row[3]}.")


def fetch_information5(name):
    sql = "SELECT Name, Municipality, Ident, Iso_country FROM airport"
    sql += " WHERE name='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:

        for row in result:
            print(f"The name of the airport is {row[0]} and it is located  in {row[1]}, {row[3]}.")


def fetch_airport_name(name):
    sql = "SELECT Name,Ident FROM airport"
    sql += " WHERE name ='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()


def fetch_airport_icao(ident):
    sql = "SELECT Ident FROM airport"
    sql += " WHERE ident ='" + ident + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()


def fetch_airport_distance(ident):
    sql = "SELECT  latitude_deg, longitude_deg from airport"
    sql += " WHERE ident ='" + ident + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return (row[0], row[1])


def fetch_information6(ident):
    sql = "SELECT Name, Municipality, Ident, Iso_country FROM airport"
    sql += " WHERE ident='" + ident + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:

        for row in result:
            print(f"{row[0]}")


# Main program
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_simulator',
    user='skamal',
    password='Villain',
    autocommit=True
)

finnavia = "efhk"
while True:

    player_firstname = input("Enter first name: ")
    if player_firstname.isalpha():
        break
    print("Please enter characters A-Z only")

while True:
    player_lastname = input("Enter last name: ")
    if player_lastname.isalpha():
        break
    print("Please enter characters A-Z only")
last_confirmation = input("Press Enter to start the game or any other characters to quit. ")


while (True):

    if last_confirmation == "":
        print("Welcome To The Game!")
        fetch_information4(finnavia)
        print("You have 10,000kg Co2 budget.")


    else:
        print("See You Again!")
        break

    print(tabulate(
        [['Hot', 'Temperature over +25C'], ['Cold', 'Temperature under -20C'], ['0DEG', 'Temperature exactly 0C'],
         ['10DEG', 'Temperature exactly +10C'], ['20DEG', 'Temperature exactly +20C'], ['CLEAR', 'Clear skies'],
         ['CLOUDS', 'Cloudy'], [' WINDY', ' Wind blows more than 10 m/s']], headers=['Weather', 'Description']))

    print("Your goal is to reach all of the airports having given weather conditions with given energy.")

    # Congratulations! One goal reached.
    # Unfortunately you did not reach any goals!
    # current weather
    # current location,
    # distance between origin and destination,
    # consumed energy,
    # available energy, achieved goals,
    # remaining goals, achieved points and
    # required points to get extra energy
    #

    # r = random.sample(display_given_weather_condition, 6)
    # rounded temp_celcius could not be read as string
    # print(r)

    remain = ["Hot", "Cold", "0DEG", "10DEG", "20DEG", "CLEAR", "CLOUDS", "WINDY"]
    available_Co2_in_kg = 20000
    print(remain)

    Co2_consumed_in_kg = 0

    list = ["efhk"]
    while available_Co2_in_kg >= 2000:
        try:
            airport = input("Enter the name of the airport or ICAO code: ").lower()

            list.append(airport)

            airportname = fetch_information6(airport)

            length = len((list))
            a = list[(length - 1)]
            b = list[(length - 2)]
            print(list)
            m = fetch_airport_distance(a)[0:2]
            n = fetch_airport_distance(b)[0:2]
            distance = GD(m, n).km
            print(f"The distance of your journey was: {distance:.2f}km")

            if airport == b:
                print("You cannot fly to your current destination!")
                print("Choose another destination.")
                continue
            if count == 8:
                break

            print(f"Total energy consumed: {Co2_consumed_in_kg + 2000}")
            Co2_consumed_in_kg = Co2_consumed_in_kg + 2000
            print(f"Remaining energy: {available_Co2_in_kg - 2000}")
            available_Co2_in_kg = available_Co2_in_kg - 2000

            icao_codes = fetch_airport_icao(airport)
            icao_codes = [icao_codes]
            airport_names = fetch_airport_name(airport)
            airport_names = [airport_names]

            fetch_information4(airport)
            fetch_information5(airport)

            lat = fetch_information2(airport)
            lon = fetch_information3(airport)

            url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=f1c5c2efcc1463620cfe351cb7b40f30&units=metric".format(
                lat, lon)

            response = requests.get(url).json()

            temp_celcius = response["main"]["temp"]

            feels_like_celcius = response["main"]["feels_like"]

            temp_celcius = round(temp_celcius)

            feels_like_celcius = round(feels_like_celcius)

            description = response["weather"][0]["description"]

            humidity = response["main"]["humidity"]
            wind = response["wind"]["speed"]

            if (temp_celcius > 25):
                greet()
                remain.remove("Hot")
                print(f"Remaining goals: {remain}")

            elif (temp_celcius < -20):
                greet()
                remain.remove("Cold")
                print(f"Remaining goals: {remain}")

            elif (temp_celcius == 0):
                greet()
                remain.remove("0DEG")
                print(f"Remaining goals: {remain}")

            elif (temp_celcius == 10):
                greet()
                remain.remove("10DEG")
                print(f"Remaining goals: {remain}")

            elif (temp_celcius == 20):
                greet()
                remain.remove("20DEG")
                print(f"Remaining goals: {remain}")

            elif (description == "clear sky"):
                greet()
                remain.remove('ClEAR')
                print(f"Remaining goals: {remain}")

            elif description == "few clouds":
                greet()
                remain.remove("CLOUDS")
                print(f"Remaining goals: {remain}")

            elif (wind > 10):
                greet()
                remain.remove("WINDY")
                print(f"Remaining goals: {remain}")

            else:
                print(f"Unfortunately! Goal not reached. \U0001F61E")
                print(f"Remaining goals: {remain}")
                break

            print(f"Temperature: {temp_celcius} degree celcius.")
            print(f"Feels like: {feels_like_celcius} degree celcius. ")
            print(f"Humidity: {humidity}.")
            print(f"Weather Description: {description}.")
            print(f"Wind: {wind}m/s.")
        except TypeError:
            if True:
                print("Invalid airport")
                list.remove(airport)

    if available_Co2_in_kg == 0:
        print(f"\033[91mEnergy Over.\nYou Lost!\nTry Again!\U0001F917\U0001F917\U0001F917")

        break