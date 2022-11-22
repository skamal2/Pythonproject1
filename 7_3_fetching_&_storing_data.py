"""Write a program for fetching and storing airport data.
The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit.
If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding
name. If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit.
(The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
You can easily find the ICAO codes of different airports online.)"""
user1 = 0
while user1 != "quit":
    airports = {"EFHK":"Helsinki Airport",
                "VNKT":"Tribhuvan Airport",
                "EDDB":"Berlin Airport",
                "OTBD":"Doha Airport"}
    user1 = input("Enter a new airport or fetch the information of an existing airport or quit: ").lower()
    if user1 =="new airport":
        ask = input("Enter the ICAO code and name of the airport: ").lower()
        user1 = input("Enter a new airport or fetch the information of an existing airport or quit: ").lower()
    if user1 == ("existing airport"):
        icao_code = input("Enter the ICAO code: ").upper()
        if icao_code in airports:
            print(f"{airports[icao_code]}")




