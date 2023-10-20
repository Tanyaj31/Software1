def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

while True:
    gallons = float(input("Type in the quantity of gasoline in American gallons (or enter a negative value to quit): "))

    if gallons < 0:
        print("Sorry, this program has now ended!")
        break

    liters = gallons_to_liters(gallons)

    print(f"{gallons} gallons is equal to {liters} liters.")
