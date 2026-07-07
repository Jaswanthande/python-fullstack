"""

    PASSING BY VALUE
    
EXAMPLE 1:
        def some(a):
            print(a+9)
        some(8)

EXAMPLE 2:
        def some(a):
            for j in a:
                print(j)
        (some([1,2,3])


RETURN KEYWORD
IN A FUNCTION IF A RETURN IS EXECUTED THE IT WILL EXIT FROM THE FUNCTION WITH CERTAIN RETURNED VALUES

    EXAMPLE
            def myfunc_(b):
                return 5 + b
            a = myfunc_(10)
            c= myfunc_(100)
            print(c)
            print(a)


    CODE FOR TO PRINT ALL BUILT IN FUNCTIONS
            import builtins
            builtin_functions =[
                name for name in dir(builtins)
                if callable(getattr(builtins,name))]
            print(builtin_functions)
            print(f"TOTAL BUILT_IN FUNCTIONS ARE (len(builtin_functions))")


RECURSIVE FUNCTION
RECURSIVE FUNCTION THAT CALLS ITSELF REPEATEDLY UNTIL A SPECIFIED CONDITION IS MET...

SYNTAX
def functio_name(parameter):
    if condition:-->base case
        return statement
    else
        return statement
print(function_name(arguments))

def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num-1)
num  = 1
print(func_name(num))




"""






















