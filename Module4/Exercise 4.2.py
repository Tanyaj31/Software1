while True:
    inches = float(input("Enter the length in inches (can be a positive or a negative value): "))
    if inches < 0:
        print("This program has ended.")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")