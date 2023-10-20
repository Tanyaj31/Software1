import random

def rolls():
    return random.randint(1, 6)

result = 0
while result != 6:
    result = rolls()
    print(f"You rolled a {result}.")

print("Wow! You rolled a 6! This game is now over. Thanks for playing!")
