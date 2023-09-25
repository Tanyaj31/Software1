i = 1
while i<11:
    print(i)
    i = i + 1

Greetings = int(input("How many greetings do you want to display?"))
first_greeting = 0
while first_greeting < Greetings:
    print("Good Morning!")
    first_greeting = first_greeting + 1
    first_greeting += 1

Greetings = int(input("How many greetings do you want to display?"))
first_greeting = 0
while first_greeting < Greetings:
    print("Good Morning!")
    first_greeting = first_greeting + 1

command=input("Tell me what to do?")
while command != "stop":
       print("Executing your command:")
       command= input("Tell me what to do? next")
print("Execution is stopped")

import random
dice1 = dice2 = real_no = 0
while(dice1 !=6 or dice2 !=6):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(dice1)
    print(dice2)
    real_no += 1
print(f"The dices were rolled {real_no} times.")

command=input("Tell me what to do?")
while command != "stop":
    if command == ("WEEKEND"):
       break
       print("Executing your command:", command)
       command= input("Tell me what to do? next")
    print("Execution is stopped")

first_no = 1
while first_no <=5:
    second_no = 1
    while second_no <=5:
        print(f"{first_no} times {second_no} is {first_no*second_no}")
        second_no += 1
    first_no += 1

import_random
number= random.randint(1,100)
guess_number= int(input("Please enter any number from 1 to 100"))
while guess_number != 100:
     if guess_number <100:
         print("The number is too low")
     elif guess_number >100:
         print("The number is too high")
     else:
         print("Hurray!!You got it!!")

