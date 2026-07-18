"""
POLYMORPHISM
POLYMORPHISM MEANS "MANY FORMS".
IT ALLOWS THE SAME METHOD, FUNCTION, OR OPERATOR TO PERFORM DIFFERENT TASKS DEPENDING ON THE OBJECT.

TYPES
1. METHOD OVERLOADING
METHOD OVERLOADING MEANS HAVING MULTIPLE METHODS WITH THE SAME NAME BUT DIFFERENT PARAMETERS.
class cal:
    def add(self,num,num2=3):
        print(num+num2)
    def add(self,num,num2=3,num3=0):
        print(num+num2+num3)
so=cal()
so.add(1,2)

2.METHOD OVERRIDING
THE METHOD OVERRIDING OCCURS WHEN A CHILD CLASS PROVIDES ITS OWN IMPLEMENTATION OF A METHOD ALREADY DEFINED IN ITS PARENT CLASS
class animal:
    def sound(self):
        print("Animal makes sounds")
class dog(animal):
    def sound(self):
        print("dog barks")
d = dog()
d.sound()

3.OPERATOR OVERLOADING
THIS ALLOWS OPERATORS (+,-,*) TO WORK DIFFERENTLY FOR USER DEFINED OBJECTS

__add__ (+)
__sub__ (-)
__mul__ (*)
__truediv__ (/)
__eq__()(==)
__It__() (<)


class student:
    def __init__(self,marks):
        self.marks =marks
    def __sub__(self,other):
        return self.marks + other.marks
s1 = student(21)
s2= student(22)
print(s1 - s2)



DATA ABSTRACTION
DATA ABSTRACTION IS THE PROCESS OF HIDING IMPLEMENTATION DETAILS AND SHOWING ONLY THE ESSENTIAL DATA TO THE USER
EG:ATM,CAR,APP

from abc import ABC,abstractmethod
class perent:
    @abstractmethod
    def display(self):
        pass


from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):
    def interest(self):
        print("SBI Interest Rate: 6.5%")

class HDFC(Bank):
    def interest(self):
        print("HDFC Interest Rate: 5.5%")

class ICICI(Bank):
    def interest(self):
        print("ICICI Interest Rate: 6.9%")
banks = [SBI(), HDFC(), ICICI()]
for bank in banks:
    bank.interest()

"""

























