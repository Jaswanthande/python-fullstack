"""
DICTIONARY
value pair seperated by  :, and keys should be unique
in the place of keys we have to use immutable datatype
dict is mutable
{}

METHODS

key()     useed to get all key from the dict                                                    SYNTAX--->variable_name.keys()
values()  used get all the values from th dict                                                  SYNTAX--->variable_name.values()
items()   used to get both key and value in a pair                                              SYNTAX--->variable_name.items()
clear()   used to get clear the dict                                                            SYNTAX--->variable_name.clear()
update()  used to update the value if it matchs name with substring then it will
          update the substring value if it does not match then it will update directly
          to dictionary 

EXAMPLES

KEYS()
details = {"name":"JASWANTH",
           "Age":56,
           "Gender":"Male"}
print(details.keys())


VALUES()
details = {"name":"JASWANTH",
           "Age":56,
           "Gender":"Male"}
print(details.values())


ITEMS()
details = {"name":"JASWANTH",
           "Age":56,
           "Gender":"Male"}
print(details.values())

CLEAR()
details ={"Name":"JASWANTH",
          "Age":56,
          "Gender": "Male"}
details.clear()
print(details)

UPDATE()
details ={"Name":"JASWANTH",
          "Age":21,
          "Gender": "Male"}
details.update({"Name":"YASWANTH"})
details.update({"Age":22})
print(details)
  


details = {"name":"JASWANTH",
           "mobile number ":8247288205,
           "adhar number":12452451125,
           "acc number":202012345854,
           "pin":"2005"}
print("WELCOME TO ATM")
user_pin=input("enter th pin")
if user_pin in details["pin"]:
    print("valid")
else:
    print("invalid")


SET
set is collection unorder elements thst are seperated by ,
set is muttable
can remove duplicate value by itself

go=(1,2,3,4,5)
print(go)

METHODS

UNION()           combines the elements from both sets                                       SYNTAX--->set_1.union(set_2)                     union symbol = |
INTERSECTION()    select the common element from the both sets                               SYNTAX--->set_1.intersection(set_2)              intersection symbol = &
SYMMETRIC()       select all the different elements from the both sets                       SYNTAX--->set_1.symmetric_difference(set_3)      symmetric_difference = ^
ADD()             used to add new elements in the set                                        SYNTAX--->variable_name.add(new_variable)
REMOVE()          used to delete the elements in the set                                     SYNTAX--->variable_name.remove(new_variable)
DISCARD()         used to delete the element if it presented in it or else it
                  will give same output if it does not present in it without any error       SYNTAX--->variable_name.discard(new_variable)


EXAMPLE


UNION()
go = {1, 2, 3, 4, 5}
so = {5, 6, 7, 8, 9, 0}
print(go | so)
print(go.union(so)))

INTERSECTION()
go = {1, 2, 3, 4, 5}
so = {5, 6, 7, 8, 9, 0}
print(go & so)
print(go.intersection(so)))

SYMMENTRIC_DIFFERENCE()
go = {1, 2, 3, 4, 5}
so = {5, 6, 7, 8, 9, 0}
print(go ^ so)
print(go.symmetric_difference(so)))

ADD()
go = {1, 2, 3, 4, 5}
go.add(6)
print(go)

REMOVE()
go = {1, 2, 3, 4, 5}
go.remove(5)
print(go)

DISCARD()
go = {1, 2, 3, 4, 5}
go.discard(9)
print(go)

"""




























