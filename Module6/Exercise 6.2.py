import random

def rolls(die_sides):
    return random.randint(1, die_sides)

die_sides = int(input("Type in the number of sides on the role-playing die!: "))

print("Now, we will roll the die:")
while True:
    result = rolls(die_sides)
    print(f"You have rolled a {result}.")
    if result == die_sides:
        break

print(f"Congratulations! You have rolled the maximum number on the dice which is {die_sides}!")
print(f"This game is now over. Thanks for playing!")
