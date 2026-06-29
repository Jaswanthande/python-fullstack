"""
TYPE CONVERSTIONS
THIS IS PROCESS OF CONVERTING ONE DATA TYPE TO ANOTHER

INT     --> String;Float
STRING  --> Integer;Float;List;Tuple
List    --> String;Tuple;Dictionary
Tuple   --> String;Lists

BUILD IN FUNCTION
str()
float()
list()
tuple()
dict()

Examples

INT     --> String;Float
num = 89
num_2 = float(num)
print(num_2)

print(type(num))
so = str(num)
print(type(so))

STRING  --> Integer;Float;List;Tuple
STRING INTO INTEGER
hi ="78"
num = int(hi)

STRING INTO FLOAT
hello ="67.8"
num_2 = float(hello)
print(num_2+num)

STRING INTO LIST
any="12345"
x=list(any)
print(x)

STRING INTO TUPLE
any="12345"
x=tuple(any)
print(x)

List    --> String;Tuple;Dictionary

LIST INTO STRING
var =['p','y','t','h','o','n']
text = "".join(var)
print(text)

LIST INTO TUPLE
var =['p','y','t','h','o','n']
var_1=[10,20,30]
text = tuple(var)
text_1 =tuple(var_1)
print(text)
print(text_1)

LIST INTO DICTIONARY
pyth = [('a',1),('b',8)]
convert = dict(pyth)
print(covert)

Tuple   --> String;Lists
TUPLE INTO STRING
hello=('j','a','s','s','u')
print(str(hello))

TUPLE  INTO LIST
"""
hello=(1,2,3)
hi =list(hello)
print(hi)



































