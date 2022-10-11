import random

import mysql.connector
from geopy.distance import geodesic as GD

import requests
def fetch_information(name):
    sql = "SELECT  latitude_deg from airport"
    sql += " WHERE name ='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :

        for row in result:

            return (row[0])

def fetch_information1(name):
    sql = "SELECT  longitude_deg from airport"
    sql += " WHERE name ='" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:

            return (row[0])


# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_simulator',
         user='skamal',
         password='Villain',
         autocommit=True
         )



player_firstname = input("Enter first name: ")
player_lasttname = input("Enter last name: ")
last_confirmation =input("Press Enter to start the game. ")
while(True):
    if last_confirmation == "":
        print("Welcome To The Game!")
        break

#The given weather conditions are:
print("Your goal is to reach all of the airports having given weather conditions with given energy.")

#Congratulations! One goal reached.
#Unfortunately you did not reach any goals!
#current weather
#current location,
# distance between origin and destination,
# consumed energy,
# available energy, achieved goals,
# remaining goals, achieved points and
# required points to get extra energy
#


given_weather_condition=[10, 19, 20, 15,  "few clouds","broken clouds", "clear sky", "overcast clouds", "windy"]
display_given_weather_condition=["10°C", "19°C", "20°C", "broken clouds", "few clouds", "clear sky", "scattered clouds", "overcast clouds"]
r=random.sample(display_given_weather_condition,6)
# rounded temp_celcius could not be read as string

print(r)
Available_Co2_in_kg = 6000
airport = input("Enter the name of the airport: ").lower()

lat= fetch_information(airport)
lon=fetch_information1(airport)


def kelvin_fahrenheit_to_celcius(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius*(9/5) + 32
    return celcius, fahrenheit
url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=f1c5c2efcc1463620cfe351cb7b40f30&units=metric".format(lat,lon)
response = requests.get(url).json()

print(response)



temp_celcius = response["main"]["temp"]

feels_like_celcius = response["main"]["feels_like"]

temp_celcius = round(temp_celcius)

feels_like_celcius= round(feels_like_celcius)

description = response["weather"][0]["description"]
humidity = response["main"]["humidity"]
wind = response["wind"]["speed"]

print(response)

if wind>=8.9:
     hawa = str("windy")
if wind<8.9:
     hawa = str(" not windy")

if temp_celcius in given_weather_condition:
    print(f"Congratulations! Goal reached!")

elif description in given_weather_condition:
    print(f"Congratulations! Goal reached!")

elif "windy" in given_weather_condition:
    print(f"Congratulations! Goal reached!")


print("Temperature: {} degree celcius.".format(temp_celcius))
print("Feels like: {} degree celcius. ".format(feels_like_celcius))
print("Humidity: {} %".format(humidity))
print("Wind Speed: {} m/s: ".format(wind) + (hawa))
print("Weather Description: {}".format(description))


