"""STATEMENTS

1.CONDITION STATEMENTS
if
if else
nested if
elif

2.CONTROL STATEMENTS
break
continue
pass

3.LOOP STATEMENTS
for
while


CONDITION STATEMENTS EXAMPLES
if statement

num=9
if num % 2 == 0:
    print(f"{num} is a even number")

if else statement
num=9
if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")

nested if statement
ATM_DETAILS = {"ATM": "3003"}
PIN = input("ENTER THE 4 DIGIT PIN:")
if len(PIN) == 4:
    if PIN in ATM_DETAILS["ATM"]:
        print(f"{PIN} is a correct pin")
    else:
        print(f"{PIN} is a incorrect pin")
print(PIN, "please enter 4 digits")

elif statement
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Failed")
    
FIND THE GREATEST AMONG THREE DIGITS

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

if a > b and a > c:
    print(f"{a} is the greatest.")
elif b > a and b > c:
    print(f"{b} is the greatest.")
else:
    print(f"{c} is the greatest.")

FINDING LETTER IS VOWEL OR NOT
a = input("enter the letter: ")
vowel = ["a","e","i","o","u"]
if a in vowel:
    print(f"{a} is a vowel")
else:
    print("constant")

FINDING MAX ELEMENT IN A LIST
n = eval(input("enter number:"))
m= max(n)
print(m)
    

"""

    
        



