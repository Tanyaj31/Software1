cities = []

for i in range(5):
    city_name = input(f"Please enter names of 5 cities one by one! {i+1}: ")
    cities.append(city_name)

print("The names of the 5 cities entered by you are as follows:")
for city in cities:
    print(city)
