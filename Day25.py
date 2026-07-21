"""
Error Handling

1.syntax error

for i in range (1,10:
    print(i)

#output-->SyntaxError

2.indentation error

    a=20
for j in range(a):
    print(j)
else:
print()

#output-->IndentationError



3.value error
num=int(input("enter a num:"))

#output-->ValueError



try
the try block will test the code for errors

syntax-->try:

except

This except let us handle the errors in the code

Syntax-->except:

example

try:
    print(num)
except:
    print('print name error')

#specific error handling
#NameError
try:
    print(num)
except NameError:
    print("will get name error")



#ValueError
try:
    num=int(input("enter a number:"))
except ValueError:
    print("will get a value a error")


#ZeroDivisionError
try:
    num=int(input("enter a number:"))
    num2=int(input("enter number2:"))
    print(num/num2)
except ZeroDivisionError:
    print("will get zerodevisionerror")




else
----
if the try block does not have error then the else block will bw executed
'''
try:
    num=int(input("enter a number:"))
    num2=int(input("enter number2:"))
    print(num/num2)
except ZeroDivisionError:
    print("will get zerodevisionerror")
except ValueError:
    print("will get value error")
else:
    print("no error")
finally:
    print("end")

"""


