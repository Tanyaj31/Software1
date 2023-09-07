import random
dots = int(input("Enter the total number of dots: "))
cp = 0
sp = 0
d1 = 0
while d1 < dots:
    randx = random.uniform(-1,1)
    randy = random.uniform(-1,1)
    distant = randx*2 + randy*2
    if distant <=1:
        cp = cp + 1
    d1 = d1 + 1
    sp = sp + 1
    pi = 4*cp/sp
print("The estimated value of pi is: ", pi)