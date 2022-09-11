import math
user = input('Give the radius of a circle: ')
radius = float(user)
pi= (math.pi)
area = float(radius*radius*(pi))
# area = float(radius*radius*(3.14))
print(f"Area of the circle is {area:.2f}")

#Next method
#import math
#radius = float(input("Enter radius: \n"))
#area = math.pi*radius
#print(f"area of a circle is: {area:.2f}")