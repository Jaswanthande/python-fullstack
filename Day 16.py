"""
    GENERATORS
    THIS GENERTOR IS SPECIAL FUNCTION THAT RETURNNS THE ITERTOR INSTEAD OF RETURNING ALL THE VALUES AT ONCES
    HERE WE ARE GOING TO USE YIELD KEYWORD

    EXAMPLE
        def some():
            yield 1
            yield 2
            yield 3
        so = some()
        print(next(so))
        print(next(so))
        print(next(so))

    WORKING OF GENERATOR
    WHEN A FUNCTION IS CALLED
    IT DOES NOT EXECUTE THE FUNCTION IMMEDIATELY
    IT WILL RETURN THE GENERATOR OBJECT
    THEN THE FUNCTION WILL PAUSES AT EACH YIELD
    WHEN next() IS CALLED AGAIN EXECUTION RESUME FROM WHERE IT STOPPED

    EXAMPLE
        def demo():
            print("start")
            yield 1
            print("middle")
            yield 2
            print("end")
            yield 3
        how = demo()
        print(next(how))
        print(next(how))
        print(next(how))

    WITH GENERATOR
        def how(hi):
            for i in range(hi+1):
                yield i*i
        so = how(5)
        print(next(so))
        print(next(so))
        print(next(so))
        print(next(so))
        print(next(so))

    WITHOUT GENERATOR
        def how(so):
            for i in range(so+1):
                print(i*i)
        how(5)

DIFFERENCE BETWEEN FUNCTION AND GENERTOR
    FUNTION
        RETURN
        RETURN COMPLET RESULT
        FUNCTION WILL END AFTER THE RETURN THE VALUES
        MORE MEMORY USAGE
        THIS FUNCTION NEVER RESUME


    GENERTOR
        YIELD
        RETURN ONE VALUE AT ONCE
        PAUSES AFTER EVERY YIELD
        LESS MEMORY USAGE
        RESUME AFTER NEXT()

    YIELD KEYWORD
        THIS WILL PRODUCES THE VALUE
        BUT THE YIELD PAUSES THE FUNCTION
        AND YIELD WILL SAVE THE FUNCTION CURRENT STATE
        YIELD WILL CONTINUES WHERE IT STOPPED

    NEXT() KEYWORD
        THE next() FUNCTION IS USED TO RETRIVE THE VALUE FROM A GENERATOR

    STOP ITERATION
        CALLING next() FUNCTION AFTER ALL VALUES RETRIEVE THEN IT WILL RAISE STOP ITERATION


    GENERATOR EXPRESSION
        THE GENERATOR EXPRESSION IS SIMILAR TO A LIST COMPREHENSION BUT USES PARENTHESIS () INSTEAD OF []
        
    EXMAPLE
        gen = (x*x for x in range(5))
        print(next(gen))
        print(next(gen))
"""

    

