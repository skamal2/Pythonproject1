
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


