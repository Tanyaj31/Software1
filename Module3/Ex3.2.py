cabin_class = input("Enter the cabin class of a cruise ship (LUX, A, B, C): ")
if cabin_class == "LUX":
    print("It is an upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("It is above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("It is a windowless cabin above the car deck.")
elif cabin_class == "C":
    print("It is a windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
