student = {
    "name": "amir",
    "grade": "A",
    "courses": ["Math","Physics", "Programming"]
}

#   Access to dictionary
print("Name:", student["name"])
print("Grade:", student["grade"])
print("Courses:", student["courses"])

# extend the dictionary
student["City"] = "Espoo"
student["age"] = 21
print(student)

#iterating through the dictionary
for key, value in student.items():
    print(key + ": ", value)

# check if a key exists in the dictionary

if 'age' in student:
 print("age found: ", student["age"])
else:
    print("Not in the dictionary")

