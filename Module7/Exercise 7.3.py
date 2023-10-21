airport_data = {}

while True:
    print("\nYour options are as follows:")
    print("1. Enter data on a new airport")
    print("2. Fetch information about an existing airport")
    print("3. Quit this program")

    choice = input("\nChoose an option: 1,2, or 3: ")

    if choice == '1':
        icao_code = input("\nEnter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")
        airport_data[icao_code] = airport_name
        print(f"\nCongratulations! Airport {icao_code} is now added to the database.")

    elif choice == '2':
        icao_code = input("\nEnter the ICAO code of the airport: ")
        airport_name = airport_data.get(icao_code)
        if airport_name:
            print(f"\nThe name of the airport with ICAO code: {icao_code} is {airport_name}.")
        else:
            print("\nSorry, but this airport is not found in the database.")

    elif choice == '3':
        print("\nThis program has now ended.")
        break

    else:
        print("\nYou have selected an invalid option. Please choose any number from 1, 2, or 3 only.")
