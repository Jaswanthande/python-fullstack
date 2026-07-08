"""
    LAMBDA FUCTION
    THIS IS ALSO CALLED AS ANNONYMOUS FUNCTION
    A LAMBDA FUNCTION FUNCTION CAN TAKE N NUMBER OF AGRUMENTS BUT Havinf only one expression

    SYNTAX  lambda agruments : expression

    FILTER()
    THE FILTER() FUNCTION IS A BUILT IN FUNCTION USED TO FILTER ELEMENTS FROM AN ITTERABLES SUCH AS LIST,TUPLE AND SET BASED ON CONDITION
    THIS FILTER() FUNCTION RETURNS FILTER OBJECT SO WE CAN CONVERT THAT INTEGER INTO LIST,SET AND TUPLE

    SYNTAX  FILTER(FUNCTION,ITTERABLE)

    EXAMPLE
    
    LAMBDA
    some =  lambda c,b : c*b
    print(some(10,4))

    FILTER()
    
    FOR EVEN NUMBERS 
    nums = [1,2,3,4,5]
    rev = filter(lambda a: a%2==0,nums)
    print(list(rev))

    FOR ODD NUMBERS
    nums = [1,2,3,4,5]
    rev = filter(lambda a: a%2!=0,nums)
    print(list(rev))


    LIST COMPREHENSION
    THIS OFFERS A SHORTER SYNTAX WHEN WE WANT TO CREATE A NEW LIST FROM THE OLD

    SYNTAX  VARIABLE_NAME = [EXPRESSION LOOP CONDITION]

    EXAMPLE
    old =[1,2,3,4,5]
    new=[j for j in old if j % 2 ==0]
    print(new)


    DICTIONARY COMPREHENSION
    THIS OFFERS A SHORTER SYNTAX WHEN WE WANT TO CREATE TO NEW DICT FROM THE OLD DICT

    SYNTAX  VARIABLE_NAME = [EXPRESSION LOOP]
    
    EXAMPLE
    old = {1:2,3:7,5:6}
    new = {i:j for (i,j) in old.items() if i % 2== 0}
    print(new)
"""










































    
