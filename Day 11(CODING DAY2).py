"""
PALINDROM
a = input("ENTER A WORD:")
b = ""
for i in a:
    b = i + b
if (b == a):
    print(f"{a} PALINDROM")
else:
    print(f"{a} NOT A PALINDROM")


FABONACCI SERIES
num = 0
num_2 = 1
limit = int(input("Enter a number: "))
print(num, num_2, end=" ")
for i in range(1,limit+1):
    all = num + num_2
    num = num_2
    num_2 = all
    print(all,end=" ")


MULTIPLY, SUBRACTION ,ADD,POWER
val = int(input("ENTER NUMBER: "))
val2 = int(input("ENTER NUMBER: "))
user = int(input("ENTER \n1.add \n2.sub \n3.mul \n4.pow:"))
if user == 1:
    print(val + val2)
elif user == 2:
    print(val - val2)
elif user == 3:
    print(val * val2)
elif user == 4 :
    print(val ** val2)
else:
    print("NOT EXITED")


TABLE
table = int(input("ENTER NUMBER:"))
for i in range(1,11):
    i = table * (i)
    print(i)


PERFECT NUMBER
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
"""



details ={"NAME":"JASWANTH",
          "PIN":"3003",
          "BALANCE": 50000}
print("----WELCOME----")
user_pin = input("ENTER THE PIN:")
if len(details["PIN"]) == 4 and user_pin ==  details["PIN"]:
    pass
else:
    print("PLEASE ENTER THE CORRECT PIN")
options = int(input("ENTER \n1.WITHDRAW \n2.DEPOSITE \n3.BALANCE :"))
if options == 1:
    n = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW:"))
    if n <= 50000 and n % 100 == 0:
        withdraw_amount = details["BALANCE"] - n
        print(f"the amount you have been withdraw is {n} and your current balance is {withdraw_amount}")
    else:
        print("YOU DOES NOT HAVE BALANCE OR YOU DOES NOT ENTER THE CORRECT AMOUNT")

elif options == 2:
    n = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSITE:"))


        


    































