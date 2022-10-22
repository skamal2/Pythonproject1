import mysql.connector

def fetch_information(ident):
    sql = "SELECT 'ident' from airport"


    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(type(result))
    if cursor.rowcount >0 :

        for row in result:
            print(f"{row[:8]}")

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
for i in range (5):
    user_input = input("Please enter the ICAO: ")
    result = fetch_information(user_input)

    if result != True:
        print("v<Invalid input")
        print()
        #user_input = input("Please enter the ICAO: ")
        #result = fetch_information(user_input)
        continue
    else result == True:
        break

print ("valid input")
