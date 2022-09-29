import mysql.connector
from geopy.distance import geodesic as GD

def fetch_information(ident):
    sql = "SELECT  latitude_deg, longitude_deg from airport"
    sql += " WHERE ident ='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:

            return (row[0],row[1])

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_simulator',
         user='skamal',
         password='Villain',
         autocommit=True
         )


ident = input("Enter first Icao code: ").upper()
ident1 = input("Enter second Icao code: ").upper()

m= fetch_information(ident)[0:2]
n= fetch_information(ident1)[0:2]
distance =GD(m,n).km

print(f"The distance between the given airports is {distance:.2f}")