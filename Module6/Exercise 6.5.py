def remove_odd_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 82, 44, 33, 87]

even_numbers_list = remove_odd_numbers(list)
print(f"The original list: {list}")
print(f"The cut-down list (without any odd numbers) is: {even_numbers_list}")
