"""
LIST

List is collection of of different datatypes that are enclosed in [] separeted by comma(,)
List is muttable

Example:
all_type =[1,"python",[1,2]]
for j in all_type:
    print(j)

Types of
1. append()     this is used to add new item into list,but it will add in the last index position
                Append will print same as u given 

2. extend()     this is also add a items into the list
                In extend it will give each char or each value gives seprate index value

3. pop()        used to delete the vallue from the list,but it will delete based on index position                  SYNTAX --> variable_name.pop(index_position)

4. remove()     used to delete the item from the list,but it will delete direct value from list                     SYNTAX --> variable_name.remove(value)
MUTTABLE                            IMMUTABLE

THE DATATYPE CAN BE MODIFIED        DATATYPE CAN'T BE MODIFIED
LIST                                STRING
EG:                                 EG:
a=[1,2,3,4,5]                       a = "python is a language"
a.append(10)                        print(a.replace("python","java",2))
print(a)                            print(a)
a.append(9)
print(a)

EXAMPLES


APPEND()
a=[1,2,3,4,5]
a.append(10)
print(a)
a.append(9)
print(a)


EXTEND()
a=[1,2,3,4,5]
a.extend([10,50])
print(a)

INDEXING EXAMPLE
a=[1,2,'Python is a language',[45,78,"Java is a language",[1,23],90],'Hello']
print(a[3][3])


POP()
a=[1,2,4,5,6,7]
a.pop(1)
print(a)


REMOVE()
a=[1,22,43,54,65,76]
a.remove(54)
print(a)


TUPLE

Tuple is collection of different datatypes represent in () and seperated by ,
it is  immutable

METHODS

1.index()
2.count()

EXAMPLE
how =(1,2,3,4,"PYTHON",[4,5],(90,78))
print(how[4])
print(how.count('PYTHON'))








"""
