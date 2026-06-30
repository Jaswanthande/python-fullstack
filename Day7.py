"""
INPUT FORMATTING FROM USER

input()
The input() function is used to take input from the user

1.int
2.string
3.float
4.list
5.tuple
6.eval

EXAMPLE

INT
num = 89
num_2 = int(input("Enter a number: "))
new= num * num_2
print(new)

STRING
a = input("Enter a string:")
print(a + "hello")

FLOAT
a = float(input("enter the salary of person 1:"))
b = float(input("enter the salary of person 2:"))
print(a+b,"is ur combin salary")

LIST
group = list(map(int,input().split()))
print(group)

TUPLE
some = tuple(map(input().split()))
print(some)
group = tuple(input().split())
print(group)

EVAL
num = eval(input("enter: "))
print(type(num))

F STRING
name = input("Enter the name:")
age = input("enter the age:")
print(name,"and my age is",age)
print(f"{name} and my age is {age}")

MODULES
name = input("Enter the name:")
age = input("enter the age:")
print("My name is %s and my age is %s"%(name,age))

"""





