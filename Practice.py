import random

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

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "f1c5c2efcc1463620cfe351cb7b40f30"
given_weather_condition=[10, 19, 20, "broken clouds", "few clouds", "clear sky", "scattered clouds"]
display_given_weather_condition=["10°C", "19°C", "20°C", "broken clouds", "few clouds", "clear sky", "scattered clouds"]
# rounded temp_celcius could not be read as string

print(display_given_weather_condition)
Available_Co2_in_kg = 6000
city = input("Enter name of the city: ")
def kelvin_fahrenheit_to_celcius(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius*(9/5) + 32
    return celcius, fahrenheit
url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(url).json()
temp_kelvin = response["main"]["temp"]
temp_celcius, temp_fahrenheit = kelvin_fahrenheit_to_celcius(temp_kelvin)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celcius, feels_like_fahrenheit = kelvin_fahrenheit_to_celcius(feels_like_kelvin)

temp_celcius = round(temp_celcius)







description = response["weather"][0]["description"]
humidity = response["main"]["humidity"]

print(response)
if temp_celcius in given_weather_condition:
    print(f"Congratulations! Goal reached!")
elif description in given_weather_condition:
    print(f"Congratulations! Goal reached!")

print("Temperature in " + (city) +": " + str(temp_celcius)+"°C")
print(f"Temperature in {city} feels like: {feels_like_celcius:.0f}°C")

print(f"General Weather in {city}: {description}")


