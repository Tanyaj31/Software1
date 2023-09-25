import math

print(math.ceil(2.9))
print(math.floor(2.98))

# next
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"The down payment is $",down_payment)

# new 345
hot_day = False
cold_day = True
if hot_day:
    print("It's a hot day")
    print("Drink plenty of water")
elif cold_day:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# not
has_good_money = True
has_good_bank = False

if has_good_money and not has_good_bank:
    print("Eligible for loan")
# comparsion operators

temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")