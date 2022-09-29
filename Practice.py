from geopy.distance import geodesic as GD
 # For the specified locations, load their latitude and longitude data.
Abuja =( 40.07080078125 , -74.93360137939453)
Dakar =(38.704022 , -101.473911)
#Finally, print the distance between the two sites in kilometers.
print("The distance between Abuja and Dakar is: ", GD(Abuja,Dakar).km)