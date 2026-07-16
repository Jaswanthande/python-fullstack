"""
SELF KEYWORD
SELF REFERS TO CURRENT OBJECT

EXAMPLE
class test:
    def display(self):
        print(self)
t = test()
print(t)
t.display()

CONSTRUCTOR
THIS CONSTRUCTOR INITIALIZES THE OBJECT AUTOMATICALLY WHEN IT IS CREATED
class batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch= branch
    def display(self):
        print(self.name)
        print(self.branch)
b4 = batch('jaswanth','ECE')
b4.display()

class fam:
    def __init__(self):
        self._name="jassu"
f = fam()
print(f._name)

#PRIVATE VARIABLE

#CALLING INSIDE THE CLASS
class bank:
    def __init__(self):
        self.__pin ="3003"
ac=bank()
print(ac._bank__pin)

#CALLING OUTSIDE THE CLASS
class bank:
    def __init__(self):
        self.__pin ="3003"
    def display(self):
        print(self.__pin)
b =bank()
b.display()


PRIVATE MEANS: __
PROTECT MEANS: _


ENCAPSULATION
Encapsulation means binding (wrapping) data (variables) and methods (functions) into a single unit (class) and restricting direct access to the data.

class ATM:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print("Updated Balance:", self._balance)
t = ATM(balance=int(input("Enter initial balance: ")))
t.deposit(amount=int(input("Enter deposit amount: ")))



class hello:
    def __init__(self,name,branch,age):
        self.name = name
        self._branch= branch
        self.__age= age
    def hi(self):
        print(self.name)
        print(self._branch)
        print(self.__age)
jassu = hello("JASWANTH","CSE","21")
jassu.hi()



class ATM:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
    def get_balance(self):
        return self._balance
atm = ATM(1000)
atm.deposit(500)
print(atm.get_balance())
"""


