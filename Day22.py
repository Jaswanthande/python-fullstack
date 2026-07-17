"""
INHERITANCEIS
INHERITANCE IS THE PROCESS IN WHICH A CHILD CLASS (DERIVED CLASS) ACQUIRES THE PROPERTIES (VARIABLES) AND BEHAVIORS (METHODS) OF A PARENT CLASS (BASE CLASS)

class parent:
    pass
class child(self):
    pass

SINGLE INHERITANCE
A CHILD CLASS INHERITS FROM ONE PARENT IS SINGLE INHERITANCE


class animal:
    def sound(self):
        print("Animals making sounds")
class dog(animal):
    def barks(self):
        print("Dog Barks")
a=dog()
a.sound()


class father:
    def land(self):
        print("Has 5 arces")
class son(father):
    def flat(self):
        print("3BHK flat")
a=son()
a.land()
a.flat()


MULTIPLE INHERITANCES
A CHILE INHERITS MORE THAN ONE PARENT IS CALLED MULTIPLE INHERITANCE
class father:
    def skills(self):
        print("driving")
class mother:
    def talent(self):
        print("cooking")
class sister:
    def learn(self):
        print("Pyhton")
class son(father,mother,sister):
    def mine(self):
        print("coding")
a=son()
a.skills()
a.talent()
a.learn()


MULTILEVEL
MULTILEVEL INHERITANCE IS A TYPE OF INHERITANCE IN WHICH A CHILD CLASS INHERITS FROM A PARENT CLASS, AND ANOTHER CHILD CLASS INHERITS FROM THAT CHILD CLASS


class grandfather:
    def house(self):
        print("Own House")
class father(grandfather):
    def flat(self):
        print("New 3bhk flat")
class son(father):
    def car(self):
        print("have a car")
fam = son()
fam.house()
fam.flat()
fam.car()

HIERARCHICAL
MULTIPLE CHILD INHERITS FROM THE SAME PARENT

class mother:
    def gold(self):
        print("10KG gold")

class mouni(mother):
    def show(self):
        print("5kg gold")

class honey(mother):
    def show_1(self):
        print("Get remaining 5KG gold")

child_1=mouni()
child_2=honey()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_1()

HYBRID INHERITANCE
THIS IS THE COMBINATION OF TWO OR MORE TYPES OF INHERITANCES
EXAMPLE OF MULTIPLE + MULTI LEVEL

class A:
    def methodA(self):
        print("Class a")
class B(A):
    def methodB(self):
        print("Class b")
class C(A):
    def methodC(self):
        print("Class c")
class D(B,C):
    def methodD(self):
        print("Class D")
hello= D()
hello.methodA()
hello.methodD()
hello.methodC()


SUPER()
THE SUPER() FUNCTION IS USED TO ACCESS THE PARENT CLASS METHOD OR CONSTRUCTOR IN THE CHILD CLASS
class parent:
    def show(self):
        print("Parent Method")
class child(parent):
    def show(self):
        super().show()
        print("Child class")
ch=child()
ch.show()

class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
a = student("jassu","101")
a.display()
"""








