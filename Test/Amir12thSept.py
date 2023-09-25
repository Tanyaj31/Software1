myTuples = (3, 35, 5)
for i in myTuples:
    print(i)
point = (2, 4)
x,y = point
print(point)
print(f"here is the x {x} value")

student = ("Timo", 22, "Computer Science")
print(f"Name:{student(0)}, Age: {student(1)}, Major: {student(2)}")
grades = (6, 8, 9, 10)
total = 0
for grade in grades:
    total += grade
print(f"Here is the total {total}")

mean = total/ (len(grades))
print(f"The mean value {mean}")

# list
students = []
students.append(("Amir",(20, 30, 40, 90, 100))
students.append(("Timo", (70, 80, 90, 100)))
students.append("Outi", (90, 98, 100, 98))

print_(students)
for student in students:
    if student[0] == "Amir":
     print(f"The name, {student[0]}")
    print(f"The grades,{student[1]}")

    found = True
    break
if not found:
    print("Sorry wrong name")
    
