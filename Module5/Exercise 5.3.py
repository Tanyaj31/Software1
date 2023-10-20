try:
    num = int(input("Type in any integer of your choice: "))

    if num <= 1:
        print(f"Sorry but {num} is not a prime number.")
    elif num == 2:
        print(f"Yes,{num} is a prime number.")
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(f"Yes, {num} is a prime number.")
        else:
            print(f"Sorry but {num} is not a prime number.")
except ValueError:
    print("You have typed in data which is not supported by us. Please enter any integer value only.")
