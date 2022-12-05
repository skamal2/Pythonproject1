from tabulate import tabulate
import mysql.connector
from prettytable import PrettyTable
def fetch_icao_codes(country_name):
    sql = 'SELECT country.name AS "Country name", airport.name AS "Airport name", airport.ident AS "ICAO Codes" FROM airport, country '
    sql += "WHERE airport.iso_country = country.iso_country AND country.name ='" + country_name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :

        for row in result:
            #print(tabulate([[row[0], row[1], row[2]]], headers=['Country name', 'Description', 'ICAO codes']))
            print(f"{row[0]}, {row[1]}, {row[2]}")

    return result

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_simulator',
         user='skamal',
         password='Villain',
         autocommit=True
         )

country_name = input("Enter country name: ")
fetch_icao_codes(country_name)