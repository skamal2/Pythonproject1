import mysql.connector

def fetch_information(first_airport, second_airport):
    names = set()
    sql = "SELECT name, type, iso_country from airport"
    sql += " WHERE iso_country='" + iso_country + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    names.add(sql)
    if cursor.rowcount >0 :

    distance=

    return

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_simulator',
         user='skamal',
         password='Villain',
         autocommit=True
         )
i=0
while i<1:
    iso_country = input("Enter area code: ").upper()
    iso_country = input("Enter area code: ").upper()
