all_numbers = []

while True:
    data = input("Type in any number (or click on enter when you're done)!: ")

    if data == "":
        break

    try:
        num = float(data)

        all_numbers.append(num)
        all_numbers.sort(reverse=True)
        all_numbers = all_numbers[:5]
    except ValueError:
        print("You have entered data which is invalid. Please type in any number only.")

if all_numbers:
    print("The five greatest numbers (entered by you) sorted in descending order are:")
    for num in all_numbers:
        print(num)
else:
    print("No numbers were entered by you.")
