"""
FILE HANLDING
FILE HANDLING IS AN OBJECT THAT GIVES MORE OPTIONS LIKE CREATING,UPDATING

TWO WAYS TO OPEN THE FILE
1.OPEN

SYNTAX
do = open("file_name","mode"):
    colse()

2.WITH KEYWORD

SYNTAX

with open ("file_name","mode") as do:

with open ("JASWANTH.txt","r")as do:
    print(do.read())


MODES

r       USED TO READ THE FILE INCASE IF THE FILE IS NOT PRESENT IT WILL RAISE ERROR
w       USED TO WRITE THE TEXT INSIDE THE FILE AND IT WILL OVERRIDE THE TEXT INSIDE FILE

EXAMPLE
with open ("JASWANTH.txt","w")as do:
    print(do.write("GOOD MORNING EVERYONE"))

a      THIS IS USED TO ADD THE TEXT AT LAST POSITION INSIDE FILE

EXAMPLE
with open("Jaswanth.txt","a")as do:
    print(do.write("HI GUYS"))

X      USED TO CREATE A NEW BY ADDING THE INSIDE THE FILE INCASE IF THE FILE IS PRESENT IT WILL RAISE AN ERROR

EXAMPLE
with open("JASWANTH.txt","x")as do:
    print(do.write("friends"))


WRITE() THIS FUNCTION IS USED TO ADD THE TEXT INSIDE A FILE OR UPDATE A FILE WITH NEW TEXT

EXAMPLE:
with open ("JASWANTH.txt","w")as do:
    print(do.write("GOOD MORNING EVERYONE"))

READ()  USED TO READ A FILE AND THIS READ() WILL BE READ FILE CHAR BY CHAR

EXAMPLE:
with open("JASWANTH.txt","r")as do:
    print(do.readline(10))

READLINE()  THIS READLINE() FUNCTION WILL READ ONLY ONE LINE AT A TIME

EXAMPLE
with open("JASWANTH.txt","r") as do:
    print(do.readline())

READLINES() THIS FUNCTION WILL READ WHOLE FILE AND GIVE IT IN A LIST EACH LINE IS ONE INDEX IN THE LIST
"""

with open("JASWANTH.txt","r") as do:
    print(do.readlines())
