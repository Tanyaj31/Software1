import random

dice_no = int(input("How many dice would you like to roll? "))

sum_of_rolls = 0

for _ in range(dice_no):
    roll = random.randint(1, 6)
    print(f"Wow! You rolled a {roll}.")
    sum_of_rolls = sum_of_rolls + roll

print(f"The sum of the rolls is: {sum_of_rolls}")
