'''
def <function>(parameters):
    """Doc String"""
    statement (s)
    #body of function
    return value(s)
fname(args) #func call

def add(a,b):
    c = a+ b
    return c
print(add(2,3))
c,d='codegnan','python'
print(add(c,d))
e,f = map(str,input("enter the value").split(','))
print(add(e,f))
print(add([1,2,3],[4,6,7]))

#variable length arguments : *args we can pass any anumbers of positional
#arguments : data will be stored in tuple

def sample(*a):
    print(a)
    print(type(a))
sample()
sample(2,3,4,5)
sample('codegnan',[23,4],'poll',2+5j)

marks = [20,15,25,18]
sample(marks)

sample(*marks)

a =21,'code','poll',1,2,6,7
print(list(a))
#print(b)
#print(c)



def add(*a):
    print(a)
    result = 0
    for i in a:
        if type(i) in [int,float]:
            result = result + i
    print(result)
print(add(2,'jaswanth',4))



def batch(name,age,place="vizag"):
    print(f'{name} is in {place} and is {age} year')
batch('Codegnan',1,'vizag')
batch(name='codegnan',place='vizag',age=21)
batch(name="jaswanth",age=21)


print(4,5,sep='-') //here keyword is sep and we are changing


def batch(**a):
    print(a)
    print(type(a))
batch()
batch(name='jaswanth',age=21,place='vizag')

data ={'names':['jaswanth','yaswanth'],
       'place':['Vskp','Hyd']}
batch(**data)

#batch(**data)
data.update({'batch':'PFS-VSP-004'})
batch(**data)

'''

#task : create a function with the usage of *args & **kwargs

def student_details(*a, **b):
    print("Subjects:", a)
    print("Student Details:", b)

student_details("Python", "SQL", "HTML",name="Jaswanth", age=21, city="Vizag")
    
    
