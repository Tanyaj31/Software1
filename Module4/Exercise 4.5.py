n = 1
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "python" and password == "rules":
        print("Welcome")
        break
    else:
        print("Incorrect username or password entered. Please try again.")
        n += 1
    if n == 6:
        print("Access Denied")
        break