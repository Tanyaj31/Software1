seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
month = int(input("Enter the number of any month ranging from 1 to 12: "))

if 1 <= month <= 3:
    season = seasons[0]
elif 4 <= month <= 6:
    season = seasons[1]
elif 7 <= month <= 9:
    season = seasons[2]
elif 10 <= month <= 12:
    season = seasons[3]
else:
    season = "Invalid month entered."

print(f"The season for month {month} is {season}.")
