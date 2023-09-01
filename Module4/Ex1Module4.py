import random
number= random.randint(1,100)
guess_number= int(input("Please enter any number from 1 to 100:"))
while guess_number != 100:
    guess_number = int(input("Please enter any number from 1 to 100:"))
    if guess_number <100:
         print("The number is too low")
    elif guess_number >100:
         print("The number is too high")
    else:
         print("Hurray!!You got it!!")