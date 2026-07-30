from datetime import datetime
current_ = datetime.now()
print(current_)
print(current_.strftime('%y'))
print(current_.strftime('%m'))
print(current_.strftime('%d'))
print(current_.strftime('%H'))
print(current_.strftime('%M'))
print(current_.strftime('%S'))
print(current_.strftime('%MS'))



from datetime import datetime,date
current_=datetime.now().today()
today=date.today()
now=datetime.now()

print(current_.strftime("%d/%m/%y %H:%M:%S %p"))
print(current_.strftime("%d/%m/%y %I:%M:%S %p"))


import calendar
print(calendar.calendar(2026))
print(calendar.month(2004,11))
print(calendar.weekday(2026,7,24))
print(calendar.isleap(2024))

'''
Data Analysis
-------------
Data analysis is the process of inspecting,cleaning,transform
and modeling data to discover useful insights , support decision
making and identify patterns . It is widely used in industries such as
finance , healthcare,marketing and technology.


types of Data analysis
----------------------

1.Descriptive Analysis - summarizing data
(eg: average sales per month)

2.Diagnostic analysis - understanding causes.
(eg: why sales dropped)

3.pedictive analysis - Forecasting future outcomes.
(eg: predicting customer churn)

4.prescriptive analysis - suggesting actions based on data
(eg: best marketing strategies).


Numpy
-----
-->Numpy is a library in python which is known as numerical python

-->This numpy have different dimentinal arrays such as 1D 2D 3D

-->To use this numpy we have to import the library as
   import numpy as np

eg
---
'''
import numpy as np

arr_1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)



#------------1D array----------#

import numpy as np
arr_1=np.array([1,2,3,4])
print(arr_1)

'''
Indexing in array
------------------
-->As we used indexing in the list or tuple,here the same way it works
-->By calling index position from the array we get the value
-->negative indexing also works
'''

#Normal indexing
import numpy as np
arr_1=np.array([1,2,3,4])
print(arr_1[2])

#Negative indexing
import numpy as np
arr_1=np.array([1,2,3,4])
print(arr_1[-1])


'''
Slicing
--------
eg
---
'''
import numpy as np
arr_1=np.array([1,2,3,4,5])
print(arr_1[:4])

import numpy as np
arr_1=np.array([1,2,3,4,5])
print(arr_1[-4:])




#---------------2D Array--------------#

import numpy as np
arr_1=np.array([[1,2,3],[4,5,6]])
print(arr_1)
print(arr_1.reshape(3,2))



#-------------3D Array----------------#

import numpy as np
arr_1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)
print(arr_1.reshape(1,9))



'''
Pandas
-------
-->pandas is a powerfull python library and this is built on the top numpy
-->by used pandas data manipulation will be done....
-->pandas have data structure like series and dataframes
-->to use this we have ti import library
import pandas as pd
'''

import pandas as pd
data=pd.Series([2000,4000,5000],['mobile','buds','chager'])
print(data)

import pandas as pd
df={
    "products":['laptop','chager','mobile'],
    'brand':['mac','realme','iphone'],
    "price":[100000,500,200000],
    'stock':[5,10,9],
    'sales':['amazon','offline','filpkart']}
so=pd.DataFrame(df)
print(so)

