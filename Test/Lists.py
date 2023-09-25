list1 = [1,2,3,4,5,"Hello"]
list2 = [1,2,3,4,5,"Hello"]
# prints 'g'
x = 'frog'
print (x[3])
# prints cow
x = ['pig', 'cow', 'horse']
print (x[1])
# add
x = 'horse' + 'shoe'
print (x)
# add two lists
x = ['pig', 'horse', 'cow'] + ['dog']
print (x)
# multiply
x= 'bug' * 3
print (x)
# multiply this
x= [6,5] * 3
print (x)
# print true
x = 'bug'
print ('u' in x)
# prints false
x = ['pig', 'cow', 'horse']
print ('cow' not in x)



names = []

name = input("Enter the first name or quit by pressing Enter: ")
while name!="":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

for n in names:
    print(f"Hello, {n}!")