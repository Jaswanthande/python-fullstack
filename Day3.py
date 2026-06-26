string
string is sequence of char that are enclosed in '',"",""" """"
str are immutable

concatenation 
here, the (+) operator act as to concatenate more than 2 string..
ex:
a = "python"
b = "is a language"
print(a +b)

indexing 
this is used to access the particular char in the string by pass index position value.
index start from 0
we have negative indexing to count the position from the last to first 
ex:
a = "python is a language"
print(a[12])

string methos 

1. replace()   This method is used to replace any substring in that particular string                                       SYNTAX --->(VAR NAME.REPLACE("OLD STRING","NEW STRING",COUNT))  
2. join()      This method used to add new substring after each char in the string                                          SYNTAX --->("STRING".JOIN(VARIABLE_NAME))
3. split()     This method used to divide the string into difference index into list, based on the string passed by us      SYNTAX --->(VAR NAME.SPLIT(SUB STRING))
4. count()     This method used to count the substring in the particular string and also specify the index position         SYNTAX --->(VAR NAME.COUNT("SUB STRING",STARTINDEX,ENDINGINDEX))

REPLACE() EXAMPLE:
a = "python is a language"
print(a.replace("python","java",2))      //string is immutable can't modify directly  // COUNT MEANS IN SENTENCES A LETTER PRESENTED IN MANY TIMES BY USING COUNT WE MAKE IT LIMIT 
print(a)

JOIN() EXAMPLE:
a = "python is a language"
PRINT("$",JOIN(SO))

SPLIT() EXAMPLE:
a = "python is a language"
print(a.split(" "))

COUNT() EXAMPLE:
a = "python is a language"
PRINT(A.COUNT("A",0,12))

STRING BUILD-IN FUNCTIONS 

1.len() This will find the length of the string, which is number char present in that string
2.max() This will find the max char in the string 
3.min()

len() EXAMPLE:
a = "python is a language"
print(len(a))

max() EXAMPLE:
a = "python is a language"
print(max(a))

min() EXAMPLE:
a = "python is a language"
print(min(a))
