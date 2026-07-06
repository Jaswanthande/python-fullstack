"""
FUNCTIONS
FUNCTION IS A BLOCK OF CODE THAT CAN BE REUABLE
FUNCTION CAN AVOID THE REPEATED LINE OF CODE

FUNCTIONS ARE TWO TYPES
1.BUILT-IN
EX PRINT(),MAX(),TYPE(),MIN(),SUM()

2.USER-DEFINE
THIS FUNCTION STARTS WITH KEYWORD (def)
def fuuction_name(parameters):
    #write the code
function_name(arguments)

    EXAMPLES:
        def function_name(a,b):
            print(a+b)
        function_name(3,4)

TYPES OF ARGUMENTS
1.REQUIRED ARGUMENTS  WE HAVE TO PASS SAME NUMBER OF ARUGUMENTS WITH DEFINATION OF THE FUNCTION 
2.DEFAULT                
3.KEYWORD             WE CAN PASS AS A PAIR LIKE (VARIABLE = DATATYPE)
4.VARIABLE LENGTH     CAN PASS N NUMBER ARGUMENTS AND JUST USE (*args) ARGS IN THE PARAMETER, WILL RECIEVE TUPLE OF ARGUMENTS
5.GLOBAL VARIABLE     A VARIABLE DECLARED OUTSIDE OF ALL FUNCTIONS OR MODULES I A PROGRAM & A VARIABLE WHICH WAS DECLARED INSIDE THE FUNCTION IS KNOWN AS LOCAL VARIABLE
NOTE : TO CHANGE THE GLOBAL VARIABLE BY USING KEYWORD (GLOBAL) THAT CAN CHANGED COMPLETLY INSIDE AND OUTSIDE OF THE FUNCTION


EXAMPLES
    REQUIRED ARGUMENTS 
        def add(a,b):
            print(a)
        add(2,3)

    DEFAULT
        num = 7
        num2=6
        num3=9
        def add(a,b,c):
            print(a)
            print(b)
            print(c)
        add(num,num2,num3)

    KEYWORD 
        def add(a,b):
            print(a+b)
        add(a=8,b=3)

        def add(a,b):
            print(a)
        add(b=9,a=6)

    VARIABLE LENGTH
    FOR * STAR
        num = 7
        num2=6
        num3=9
        def add(*a):  (* means to transfer values into tuples
            print(a)
        add(num,num2,num3)

   FOR ** STAR
        def all_(**any):
            print(any["AGE"])
        all_(NAME = "JASWANTH",AGE = 14)

   GLOBAL VARIABLE 
        num = 30
        def func():
            print(num)
        func()

   THIS CODE IS USED FOR CHANGING THE GLOBAL VARIABLE INSIDE THE FUNCTION
        num = 30
        def func():
            global num
            num = 85
            print(num)
        func()


"""

num = 30
def func():
    global num
    num = 85
    print(num)
func()

































    
