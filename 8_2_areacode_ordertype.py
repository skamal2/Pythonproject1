import mysql.connector

def fetch_information(iso_country):
    sql = "SELECT name, type, iso_country from airport"
    sql += " WHERE iso_country='" + iso_country + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :

        for row in result:
            print(f"{row[0]} {row[1]}")

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

iso_country = input("Enter area code: ").upper()
fetch_information(iso_country)