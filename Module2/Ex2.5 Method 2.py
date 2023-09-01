Pounds_Per_Talent = 20
Lots_Per_Pound = 32
Grams_Per_Lot = 13.3
Talents = float(input("\nEnter a mass in talents:\n"))
Pounds = float(input("\nEnter a mass in pounds:\n"))
Lots = float(input("\nEnter a mass in lots:\n"))
Total_lots = (Talents * Pounds_Per_Talent + Pounds) * Lots_Per_Pound + Lots
grams = Total_lots * Grams_Per_Lot
kilograms = int(grams // 1000)
grams %= 1000
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")