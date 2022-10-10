import requests

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "f1c5c2efcc1463620cfe351cb7b40f30"
city = input("Enter name or the ICAO code of your destination: ").upper()
def kelvin_fahrenheit_to_celcius(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius*(9/5) + 32
    return celcius, fahrenheit


url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(url).json()
temp_kelvin = response["main"]["temp"]
temp_celcius, temp_fahrenheit = kelvin_fahrenheit_to_celcius(temp_kelvin)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celcius, feels_like_farenheit = kelvin_fahrenheit_to_celcius(feels_like_kelvin)

description = response["weather"][0]["description"]
humidity = response["main"]["humidity"]


print(f"Temperature in {city}: {temp_celcius:.0f}°C")
print(f"Temperature in {city} feels like: {feels_like_celcius:.0f}°C")

print(f"General Weather in {city}: {description}")
