import random
number_1 = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input("Guess the number between 1 and 10: "))
    attempts += 1
    if guess == number_1:
        print(f"Correct! You guessed the right number in {attempts} attempts.")
        break
    elif guess < number_1:
        print("Too low. Please try again.")
    else:
        print("Too high. Please try again.")