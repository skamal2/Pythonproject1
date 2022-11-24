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

####Api practices

"""response = requests.get("http://randomfox.ca/floof")
print(response.status_code)#The HTTP 200 OK success status response code indicates that the request has succeeded.
print(response.text)#To get data in nice readable format
#json is part of request, it is the language used by api to convert txt data into python dictionary.
fox = response.json()
print(fox['image'])"""
import pprint
########
"""url = "https://api.tvmaze.com/singlesearch/shows?q=girls"
parameters = {"q": "Girls"}

response = requests.get(url, parameters)
if response.status_code == 200:
    #print(response.text)
    #This looks like dictionary but actually is not a dictionary.
    #so to convert response.txt into dictionary we use json.
    data = json.loads(response.text)
    #pprint.pprint(data)
    #pprint makes data easy to read
    #lets pull out name premiered and summary
    name = data['name']
    premiered = data['premiered']
    summary = data['summary']

    print(f"{name} premiered on {premiered}.")
    print(summary)

else:
    print(f"Error: {response.status_code}")"""

####

"""url = "https://api.tvmaze.com/singlesearch/shows?q=Star Trek"
response = requests.get(url)
if response.status_code == 200:
    #print(response.text)
    #This looks like dictionary but actually is not a dictionary.
    #so to convert response.txt into dictionary we use json.
    data = json.loads(response.text)
    #pprint.pprint(data)
    #pprint makes data easy to read
    #lets pull out name premiered and summary
    name = data['name']
    premiered = data['premiered']
    summary = data['summary']

    print(f"{name} premiered on {premiered}.")
    print(summary)

else:
    print(f"Error: {response.status_code}")"""

#######For user input

"""url = "https://api.tvmaze.com/singlesearch/shows"
show = input("please input a show name: ")
parameters= {"q":show}

response = requests.get(url, parameters)
if response.status_code == 200:
    #print(response.text)
    #This looks like dictionary but actually is not a dictionary.
    #so to convert response.txt into dictionary we use json.
    data = json.loads(response.text)
    #pprint.pprint(data)
    #pprint makes data easy to read
    #lets pull out name premiered and summary
    name = data['name']
    premiered = data['premiered']
    summary = data['summary']
    schedule =data['schedule']['time']

    print(f"{name} premiered on {premiered} & the schedule is {schedule}.")
    print(summary)

else:
    print(f"Error: {response.status_code}")"""