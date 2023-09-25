def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

while True:
    user_input = int(input("Please enter an integer number (can be positive or negative): "))

    if user_input <= 0:
     print("Execution ends.")
     break
    else:
     result = factorial(user_input)
     print(f"The factorial of {user_input} is {result}")
