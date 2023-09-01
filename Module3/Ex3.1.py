zander_length = int(input("Enter the length of the zander in centimeters: "))

size_limit = 42

if zander_length >= size_limit:
    print("Congratulations! The zander meets the size limit.")
else:
    difference = size_limit - zander_length
    print("The zander is below the size limit.")
    print(f"Release the fish back into the lake. It was {difference} centimeters below the size limit.")