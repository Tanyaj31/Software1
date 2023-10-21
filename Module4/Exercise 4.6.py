import random

dots = int(input("Type in the total number of dots: "))
cp = 0

for _ in range(dots):
    randx = random.uniform(-1, 1)
    randy = random.uniform(-1, 1)
    distant = randx ** 2 + randy ** 2
    if distant <= 1:
        cp = cp + 1

pi = 4 * cp / dots

print("The estimated value of pi (π) is:", pi)
