names = set()

all_names = []

while True:
    name = input("Type in a name (or click on Enter when you're done to view the list of names): ")

    if name == "":
        break

    if name in names:
        print("Existing name:")
    else:
        print("New name:")
        names.add(name)

    all_names.append(name)

print("\nThe list of names typed in by you are as follows:")
for name in all_names:
    print(name)
