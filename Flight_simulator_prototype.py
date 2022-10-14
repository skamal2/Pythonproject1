import random

import mysql.connector
from geopy.distance import geodesic as GD

import requests

count = 0


def greet():
    print(f"Congratulations! Goal reached! \U0001f600")
    global count
    count += 1

    if count == 4:
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
            print(f"The name of the airport is {row[0]} and it is located  in {row[1]}, {row[3]}.")


def fetch_information5(name):
    sql = "SELECT Name, Municipality, Ident, Iso_country FROM airport"
    sql += " WHERE name='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:

        for row in result:
            print(f"The name of the airport is {row[0]} and it is located  in {row[1]}, {row[3]}.")


# Main program
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_simulator',
    user='skamal',
    password='Villain',
    autocommit=True
)

player_firstname = input("Enter first name: ")
player_lasttname = input("Enter last name: ")
last_confirmation = input("Press Enter to start the game. ")
while (True):
    if last_confirmation == "":
        print("Welcome To The Game!")
        print("Starting point is: Helsinki Vantaa airport")
        break

# The given weather conditions are:
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


given_weather_condition = [20, 15, "broken clouds", "clear sky"]
display_given_weather_condition = ["20°C", "15°C", "broken clouds", "clear sky"]
#r = random.sample(display_given_weather_condition, 6)
# rounded temp_celcius could not be read as string
#print(r)
print(display_given_weather_condition)
available_Co2_in_kg = 10000


Co2_consumed_in_kg = 0
while available_Co2_in_kg >=2000:
    if count == 4:
        break

    print(f"Total energy consumed: {Co2_consumed_in_kg}")
    Co2_consumed_in_kg = Co2_consumed_in_kg + 2000
    print(f"Remaining energy: {available_Co2_in_kg}")
    available_Co2_in_kg = available_Co2_in_kg - 2000





    airport = input("Enter the name of the airport or ICAO code: ").lower()

    fetch_information4(airport)
    fetch_information5(airport)

    lat = fetch_information(airport) or fetch_information2(airport)
    lon = fetch_information1(airport) or fetch_information3(airport)

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


    if temp_celcius in given_weather_condition:
        greet()
        given_weather_condition.remove(temp_celcius)
        print(f"Remaining goals: {given_weather_condition}")

    elif description in given_weather_condition:
        greet()
        given_weather_condition.remove(description)
        print(f"Remaining goals: {given_weather_condition}")

    else:
        print(f"Unfortunately! Goal not reached. \U0001F61E")
        print(f"Remaining goals: {given_weather_condition}")

    print("Temperature: {} degree celcius.".format(temp_celcius))
    print("Feels like: {} degree celcius. ".format(feels_like_celcius))
    print("Humidity: {} %".format(humidity))
    print("Weather Description: {}".format(description))




    if available_Co2_in_kg==0:
        print(f"\033[91mEnergy Over.\nYou Lost!\nTry Again!\U0001F917\U0001F917\U0001F917")

