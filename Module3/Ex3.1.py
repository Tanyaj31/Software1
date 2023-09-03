zander_length = int(input("Please enter the length of the zander in centimeters: "))
if zander_length >=42:
    print("Congratulations! The zander meets the size limit.")
else:
    difference = 42 - zander_length
    print("The zander is below the size limit.")
    print(f"Release the fish back into the lake. It was {difference} centimeters below the size limit.")