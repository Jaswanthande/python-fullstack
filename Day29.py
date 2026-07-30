'''
Matplot
_______

Matplotlib library is an python library that provides functionality to charts,
graphs,bar and data visualization
'''
#LINE GRAPH
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,15,30,5]

plt.plot(x,y)
plt.title("sales of BMW")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


import matplotlib.pyplot as loki
x=[2020,2021,2022,2023,2024,2025,2026]
y=[23,56,33,12,85,98,45]

loki.plot(x,y)
loki.title("sales")
loki.xlabel("Year")
loki.ylabel("sales")
loki.show()


#BAR GRAPH
import matplotlib.pyplot as sai
x=['bmw','audi','benz','honda','suzuki']
y=[12,55,65,23,90]

sai.figure(facecolor='yellow')#add color to the figure bg
sai.bar(x,y,color='black',edgecolor='blue')
sai.gca().set_facecolor('pink')#add colour to the graph bg
sai.title("car sales")
sai.xlabel("car brand")
sai.ylabel("sales")
sai.show()


#PIE CHART
import matplotlib.pyplot as loki
subject_=['python','java','c']
stu_=[20,50,50]

loki.pie(stu_,labels=subject_,colors=['black','blue','yellow'],autopct='%1.1f%%')
loki.legend(subject_)
loki.title('courses')
loki.show()


#SCATTER PLOT
import matplotlib.pyplot as loki
x=['bmw','audi','benz','honda','suzuki']
y=[12,55,65,23,90]

loki.scatter(x,y,color='black')
loki.title("sales of cars")
loki.xlabel('brand')
loki.ylabel('sales')
loki.show()


#ALL GRAPHS
import matplotlib.pyplot as loki
x=['bmw','audi','benz','honda','suzuki']
y=[12,55,65,23,90]

loki.figure()

loki.subplot(2,3,1)
loki.plot(x,y)

loki.subplot(2,3,2)
loki.bar(x,y)

loki.subplot(2,3,3)
loki.pie(y,labels=x)

loki.subplot(2,3,4)
loki.scatter(x,y)

loki.subplot(2,3,5)
loki.hist(y,bins=20)
loki.show()


#HISTOGRAM
import matplotlib.pyplot as loki
x=[10,40,20,50]
loki.hist(x,bins=30)
loki.xlabel('years')
loki.ylabel('no of cars')
loki.show()

