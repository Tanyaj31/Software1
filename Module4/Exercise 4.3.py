smallest_number = None
largest_number = None
while True:
    input_number = input("Enter a number or click Enter to quit: ")
    if input_number == "":
        break

    number = float(input_number)
    if smallest_number is None or number < smallest_number:
        smallest_number = number
    if largest_number is None or number > largest_number:
        largest_number = number

if smallest_number is not None and largest_number is not None:
    print(f"The smallest number is: {smallest_number}")
    print(f"The largest number is: {largest_number}")