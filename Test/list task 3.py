shopping_List = [] #list for store shopping
while True:
    item = input("Enter the item for your shopping list (type 'done' to finish): ")
    if item =='done':
        break
    shopping_List.append(item)
print("Your shopping list:")
for item in shopping_List:
    print(item)



