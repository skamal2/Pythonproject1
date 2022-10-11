import mysql.connector

def fetch_information(ident):
    sql = "SELECT Name, Municipality, Ident FROM airport"
    sql += " WHERE ident='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :

        for row in result:

            print(f"The name of the airport is {row[0]} and it is located  in {row[1]}.")


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

ident = input("Enter ICAO code: ").upper()

fetch_information(ident)
