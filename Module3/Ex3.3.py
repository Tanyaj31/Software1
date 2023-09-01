gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if 117 <= hemoglobin <= 155:
        result = "normal"
    elif hemoglobin < 117:
        result = "low"
    else:
        result = "high"
elif gender == "male":
    if 134 <= hemoglobin <= 167:
        result = "normal"
    elif hemoglobin < 134:
        result = "low"
    else:
        result = "high"
else:
    result = "unknown gender"

print(f"The hemoglobin value for the mentioned {gender} is {result}.")