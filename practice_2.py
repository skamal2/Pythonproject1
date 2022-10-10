import mysql.connector

def fetch_information(ident):
    sql = "SELECT ident, lattitude_deg, longitude_deg from airport"
    sql += " ident='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :

        for row in result:
            print(f"The distance between given airport is: {row[1],row[2]}")
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

ident = input("Enter Icao code: ").upper()
fetch_information(ident)
