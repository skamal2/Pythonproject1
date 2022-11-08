def get_city_name():
    city= input("Enter the name of the city: ")
    return city

def get_temp_in_kelvin(city,key):
    request= "https://api.openweathermap.org/data/2.5/weather?g=" + city+ f"&APPIO={key}"
    response= request.get(request).json()
    kelvin= response['main']['temp']
    return kelvin

def kelvin_to_celsius(kelvin):
    return kelvin-273.15

city= get_city_name()
key = input("Enter your API key: ")
celsius= kelvin_to_celsius(get_temp_in_kelvin(city,key))
print(f"The temperature in {city} is {round(celsius, 1)} degree Celsius.")