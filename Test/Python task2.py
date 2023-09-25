grades = []
while True:
    grade = input("Enter a grade (-1 to infinity): ")
    if grade == "-1":
        break
        grades.append(grade)
        grades.clear
        print("The program has ended")
    else:
        print("")
