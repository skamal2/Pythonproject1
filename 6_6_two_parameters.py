import math
def main(diameter, price):

    return (diameter*price)
user=float(input("Enter the diameter of the pizza in centimeters: \n"))
radius_in_meters= user/200
size=((math.pi)*(radius_in_meters)**2)
per_square_meter_price_of_pizza_pollo=5
per_square_meter_price_of_hawain_pizza=6
price_for_customer_for_pizza_pollo=(math.pi)*((radius_in_meters)**2)*per_square_meter_price_of_pizza_pollo
price_for_customer_for_hawain_pizza=(math.pi)*((radius_in_meters)**2)*per_square_meter_price_of_hawain_pizza
print(f"Tthe price of a pizza pollo is {main(size,per_square_meter_price_of_pizza_pollo):.2f}")
print(f"The size of a hawain pizza is {main(size,per_square_meter_price_of_hawain_pizza):.2f}")


