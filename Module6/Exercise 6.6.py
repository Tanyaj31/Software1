def calculate_pizza_area(diameter_cm):
    radius_cm = diameter_cm / 2
    area_cm2 = 3.14 * radius_cm ** 2
    area_m2 = area_cm2 / 10000
    return area_m2

def calculate_unit_price(diameter_cm, price_euros):
    area_m2 = calculate_pizza_area(diameter_cm)
    unit_price = price_euros / area_m2
    return unit_price

print("Please enter details for the first pizza:")
diameter1 = float(input("Enter the diameter (in centimeters) of the pizza: "))
price1 = float(input("Enter the price (in euros) of the pizza: "))

print("\nPlease enter details for the second pizza:")
diameter2 = float(input("Enter the diameter (in centimeters) of the pizza: "))
price2 = float(input("Enter the price (in euros) of the pizza: "))

unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money as it has a lower unit price.")
elif unit_price1 > unit_price2:
    print("The second pizza provides better value for money as it has a lower unit price.")
else:
    print("Both of the pizzas have the same unit price.")
