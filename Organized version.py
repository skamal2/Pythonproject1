import random
import sys
import mysql.connector
from geopy.distance import geodesic as GD
from tabulate import tabulate

import requests


count = 0

#greet function is created for counting goals, so that after certain goals, winner is determined.
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


def for_latitude_from_icao(ident):
    sql = "SELECT  latitude_deg from airport"
    sql += " WHERE ident ='" + ident + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:

        for row in result:
            return (row[0])


def for_longitude_from_icao(ident):
    sql = "SELECT  longitude_deg from airport"
    sql += " WHERE ident ='" + ident + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return (row[0])


def for_name_location_of_user_input(ident):
    sql = "SELECT Name, Municipality, Ident, Iso_country FROM airport"
    sql += " WHERE ident='" + ident + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:

        for row in result:
            print(f"Current location: The name of the airport is {row[0]} and it is located  in {row[1]}, {row[3]}.")


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


def name_of_airport(ident):
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

vantaa_airport_icao = "efhk"
#To include in list for current location.
while True:

    player_firstname = input("Enter first name: ")
    #To accept only A to Z character from user.
    if player_firstname.isalpha():
        break
    print("Please enter characters A-Z only")

while True:
    player_lastname = input("Enter last name: ")
    # To accept only A to Z character from user.
    if player_lastname.isalpha():
        break
    print("Please enter characters A-Z only")
last_confirmation = input("Press Enter to start the game or any other characters to quit. ")

#given_weather_condition = [["  Very Hot  ", "    Windy       ", "Freezing Cold", "clear sky"],
                         #["Weather>30°C", "Wind speed>10m/s", "Weather<0°C  ", "No clouds"]]

while (True):

    if last_confirmation == "":
        print("Welcome To The Game!")
        for_name_location_of_user_input(vantaa_airport_icao) #to inform user that current location is airport.
        print("You have 10,000kg Co2 budget.")
    # to inform user Co2 budget.

    else: #if user type any other character than enter.
        print("See You Again!")
        break #End execution of prgram.
#tabulate creates table like structure.
    print(tabulate(
        [['Hot', 'Temperature over +25C'], ['Cold', 'Temperature under -20C'], ['0DEG', 'Temperature exactly 0C'],
         ['10DEG', 'Temperature exactly +10C'], ['20DEG', 'Temperature exactly +20C'], ['CLEAR', 'Clear skies'],
         ['CLOUDS', 'Few clouds'], [' WINDY', ' Wind blows more than 10 m/s']], headers=['Weather', 'Description']))

    # The given weather conditions.
    print("Your goal is to reach all of the airports having given weather conditions with given energy.")

    remain=["HOT","COLD","0DEG","10DEG","20DEG","CLEAR", "CLOUDS","WINDY"]
    co2_budget = 10000
    print(remain)

    consumed_co2 = 0

    list_of_user_input = ["efhk"]
    while co2_budget >0:
        try:
            airport = input("Enter  ICAO code of the airport: ").lower()

            list_of_user_input.append(airport)


            airportname = name_of_airport(airport)

            icao_list_length = len((list_of_user_input))
            previous_destination = list_of_user_input[(icao_list_length - 1)]
            current_destination = list_of_user_input[(icao_list_length - 2)]
            print(f"Icao codes of your starting point and what you have typed so far: {list_of_user_input}")
            last_location = fetch_airport_distance(previous_destination)[0:2]
            current_location = fetch_airport_distance(current_destination)[0:2]
            distance = GD(last_location, current_location).km
            #distance=distance between current location and last location.

            print(f"The distance of your journey was: {distance:.2f}km")
            fuel_consumption_factor = 0.09 * distance
            #9kg fuel for 100km.
            if airport == current_destination:
                print("You cannot fly to your current destination!")
                print("Choose another destination.")
                continue

            # count is used for counting goals achieved, greet function is created for that.
            total_energy_consumption = consumed_co2 + fuel_consumption_factor
            if total_energy_consumption>=10000:
                total_energy_consumption = 10000
            print(f"Total energy consumed: {total_energy_consumption}")
            consumed_co2 = consumed_co2 + fuel_consumption_factor
            remaining_energy = co2_budget - fuel_consumption_factor
            if remaining_energy<=0:
                remaining_energy=0
            print(f"Remaining energy: {remaining_energy}")
            co2_budget = co2_budget - fuel_consumption_factor
            #for informing about fuels to players.



            icao_codes = fetch_airport_icao(airport)

            airport_names = fetch_airport_name(airport)


            for_name_location_of_user_input(airport)


            lat = for_latitude_from_icao(airport)
            lon = for_longitude_from_icao(airport)
            #for api url

            url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=f1c5c2efcc1463620cfe351cb7b40f30&units=metric".format(
                lat, lon)

            response = requests.get(url).json() #create complete url

            temp_celcius = response["main"]["temp"]

            feels_like_celcius = response["main"]["feels_like"]

            temp_celcius = round(temp_celcius)

            feels_like_celcius = round(feels_like_celcius)

            description = response["weather"][0]["description"]

            humidity = response["main"]["humidity"]
            wind = response["wind"]["speed"]


            if (temp_celcius > 25) and (("HOT") in remain):
                greet()
                remain.remove("HOT")
                print(f"Remaining goals: {remain}")

            elif (temp_celcius < -20) and ("COLD" in remain):
                greet()
                remain.remove("COLD")
                print(f"Remaining goals: {remain}")

            elif (temp_celcius == 0) and ("0DEG" in remain):
                greet()
                remain.remove("0DEG")
                print(f"Remaining goals: {remain}")

            elif (temp_celcius == 10) and ("10DEG" in remain):
                greet()
                remain.remove("10DEG")
                print(f"Remaining goals: {remain}")

            elif (temp_celcius == 20) and ("20DEG" in remain):
                greet()
                remain.remove("20DEG")
                print(f"Remaining goals: {remain}")

            elif (description == "clear sky") and ("CLEAR" in remain):
                greet()
                remain.remove('CLEAR')
                print(f"Remaining goals: {remain}")

            elif description == "few clouds" and ("CLOUDS" in remain):
                greet()
                remain.remove("CLOUDS")
                print(f"Remaining goals: {remain}")

            elif (wind > 10) and ("WINDY" in remain):
                greet()
                remain.remove("WINDY")
                print(f"Remaining goals: {remain}")

            else:
                print(f"Unfortunately! Goal not reached. \U0001F61E")
                print(f"Remaining goals: {remain}")

            print(f"Temperature: {temp_celcius} degree celcius.")
            print(f"Feels like: {feels_like_celcius} degree celcius. ")
            print(f"Humidity: {humidity}.")
            print(f"Weather Description: {description}.")
            print(f"Wind: {wind}m/s.")

        except TypeError:
            if True:
                print("Invalid airport")
                list_of_user_input.remove(airport)
        if count == 8:
            break
    if count == 8:
        break

    if remaining_energy < (fuel_consumption_factor) : #does not work because of above while loop
        print(f"\033[91mEnergy Over.\nYou Lost!\nTry Again!\U0001F917\U0001F917\U0001F917")

        break