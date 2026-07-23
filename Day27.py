"""
1.findall()

IT WILL FIND ALL THE CHAR THAT ARE IN THE STRING...

EXAMPLE

import re
txt = 'HELLO GUYS GOOD MORNING'
print(re.findall('a',txt))

import re
txt = 'sanjay rocky loves kgf 1009034'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))



2.search()

IT WILL FIND THE CHAR BUT IT WILL BE AT THE FIRST SEQUENCE THAT FOUND IN THE STRING

EXAMPLE
import re
txt = 'HELLO GUYS GOOD MORNING'
print(re.search('[a]',txt))

3.split()

EXAMPLE
import re
txt = 'HELLO GUYS GOOD MORNING'
print(re.split(' ',txt))

4.sub()

EXAMPLE
import re
txt = 'HELLO GUYS GOOD MORNING'
print(re.sub(' ','&',txt))

5.full match()



import re
txt = 'HELLO GUYS good MORNING 123'
print(re.search('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))
metachar
--------
[]
^
$
.
*
+
{}
EXAMPLES:

($) 
import re
some = "HELLO GUYS GOOD MORNING"
print(re.findall("MORNING$", some))
print(re.search("MORNING$",some))

(.)
import re
some = "HELLO GUYS GOO MORNING"
print(re.findall("G..", some))
print(re.search("G...",some))

(*)
import re
some = "HELLO GUYS GOO MORNING"
print(re.findall("H.*O", some))
print(re.findall("H.*ELLO",some))

(+)
import re
now = "HELLO GUYS GOO MORNING"
print(re.findall("H.+O",now))
print(re.findall("H.+LLO",some))
print(re.findall("H.+ELLO",some))

{}
import re
now = "HELLO GUYS GOO MORNING"
print(re.findall("H.{1}",now))
"""
{}
import re
now = "HELLO GUYS GOO MORNING"
print(re.findall("H.{1}",now))
print(re.findall("H.{20}",now))
