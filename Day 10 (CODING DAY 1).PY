"""
GENERATE PRIME NUMBER

num = int(input("enetr a number:"))
count = 0
for i in range(1, num +1):
    if num % i ==0:
          count += 1
if count == 2:
        print(f"{num}it is prime number")
else:
    print(f"{num} it is not a prime number")


GENERATE PRIME NUMBER IN A RANGE
limit =100
for i in range(1, limit+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f"{j} is a prime number")


GENERATE RIGHT ANGLE TRIANGLE USING STARS
num = 5
for i in range(1,num + 1):
    for i in range (1,i+ 1):
        print("*", end = " ")
    print()


GENERATE RIGHT ANGLE TRIANGLE USING NUMBERS
num = 5
for i in range(1,num + 1):
    for j in range (1,i+ 1):
        print(i, end = " ")
    print()

num = 5
for i in range(1,num + 1):
    for j in range (1,i+ 1):
        print(j, end = " ")
    print()

num = 5
count = 0
for i in range(1,num + 1):
    for j in range (1,i+ 1):
        count += 1
        print(count, end = " ")
    print()

num = 5
count = 0
for i in range(num,0,- 1):
    for j in range (1, i+1):
        count += 1
        print(j, end = " ")
    print()


AMSTRONG NUMBER
a = int(input("enter a number"))
length = len(str(a))
b = 0
for i in str(a):
    b += int(i) ** length
if b == a:
    print(f"{a} is amstrong number")
else:
    (f"{a} is amstrong number")

PYRIMIDE
num =10
for j in range(num):
    print(" " *(num - j - 1),end=" ")
    print("*" *(2 * j + 1)) #

"""



          
          
