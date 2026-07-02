"""
LOOPS

1.for loop         FOR IS USED TO ITTERATE OVER A SEQUENCE ,LIST,TUPLE

else in for loop   ELSE BLOCK WILL BE EXECUTED AFTER THE LOOP BUT IN A CASE THE LOOP IS BREAKED THEN IT WILL NEVER ENTERED IN THE ELSE

range()            RANGE () IS A IN BUILD FUNCTION THAT IS USED TO GENERATE A SQUENCE UPTO USER GIVEN RANGE           SYNTAX--->RANGE(START, END , STEP)   

assert keyword     IT WILL USED TO CHECK THE CONDITION,BUT IT WILL RAISE AN ERROR INCASE IT IS FALSE

2.while loop       THE WHILE LOOP WILL EXECUTED UNTILL THE CONDITION BECOMES TRUE

EXAMPLE

FOR LOOP USING ON STRING
any ="JASWANTH"
for i in any:            #HERE I IS ISTANCE VARIABLE 
    print(i)

FOR LOOP USING ON LIST
any =[1,2,4,6,78]
for i in any:
    print(i)

FOR LOOP USING ON TUPLE
any =(1,2,4,6,78)
for i in any:
    print(i)

FOR LOOP USING ON DICT
any ={"NAME": "JASWANTH"
      ,"NUMBER":8247288205}
for i in any.values():
    print(i)

ELSE IN FOR LOOP
any =(1,2,4,6,78)
for i in any:
    print(i)
else:
    print("program ended")

RANGE
a=[1,2,3,4,5]
for i in range(1,50):
    print(i)

ASSERT KEYWORD
num = int(input("ENTER YOUR AGE:"))
assert num > 0,"YOU MUST HAVE 18 YEARS"

WHILE
i=1
while i <= 5:
    print(i)
    i +=1



CONNDITION STATEMENT

1.BREAK     THE BREAK IS USED EXIT FROM THE LOOP
2.CONTIUNE  THE CONTINUE WILL SKIP THE CURRENT ITTERATION
3.PASS      THE PASS IS A SPACE HOLDER


EXAMPLE


BREAK
any =[2,4,6,8,9]
for i in any:
    if i == 6:
        break
    print(i)
else:
    print("entered")


CONTINUE
any =[2,4,6,8,9]
for i in any:
    if i == 6:
        continue
    print(i)
else:
    print("entered")

PASS
any =[2,4,6,8,9]
for i in any:
    if i == 6:
        pass


"""
a=[1,2,3,4,5]
for i in range(1,101):
    if i % 2 == 0:
        print(i)
        i += 1

    






























