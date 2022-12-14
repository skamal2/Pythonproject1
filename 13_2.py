
# Exercise 2
from flask import Flask, request
import json
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_simulator',
         user='root',
         password='Villain',
         autocommit=True
     )

def find_airport_and_location_by_icao(icao):
    sql = 'SELECT airport.name, country.name from airport join country using (iso_country)'
    sql += ' WHERE ident = "' + icao + '"'
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    print(result)
    return result[0][1], result[0][0]

app = Flask(__name__)
@app.route('/airport/<icao>')
def get_airport(icao):
    country  =""
    name = ""

    # number = int(args.get("number"))

    try:
        country, name = find_airport_and_location_by_icao(icao)

        response = {
            "icao" : icao,
            "airport_name" : name,
            "location" : country
        }

        # json_data = json.dumps(response, default=lambda o: o.__dict__, indent=4)

        # return response
        return response
    except:
        return "Airport Not Found"

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
