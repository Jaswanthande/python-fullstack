''''
marks =[]
for i in range(3):
    mark = int(input())
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
removed_mark = marks.pop()
print(f'Removed mark is {removed_mark}')
print(marks)
print(f'count of the list {len(marks)}')



numbers = [20, 10, 30, 20, 40, 20]
numbers.sort()
print(f'Ascending order :{numbers}')
numbers.reverse()
print(f'Descending order :{numbers}')
search = int(input("Enter th enumber"))
if search in numbers:
    print("Element is found")
    print(numbers.count(search))
    print(numbers.index(search))
print(max(numbers))
print(min(numbers))
print(sum(numbers))



user_input=int(input("Enter the value"))
for i in range(user_input):
    weight = float(input("Enter the weight in kgs: "))
    height = float(input("Enter the height in meters: "))
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        print(bmi)
        if bmi <= 18.5:
            print(f"{bmi} is underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            print(f"{bmi} is normal weight")
        elif bmi >= 25 and bmi <= 29.9:
            print(f"{bmi} is overweight")
        elif bmi >= 30:
            print(f"{bmi} is obese")
    else:
        ("enter only positive values!!!!!!!")


hello = []
user_input=int(input("Enter the value:"))
for i in range(user_input):
    weight = float(input("Enter the weight in kgs: "))
    height = float(input("Enter the height in meters: "))
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        hello.extend([weight,height])
        print(bmi)
        if bmi <= 18.5:
            print(f"{bmi} is underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            print(f"{bmi} is normal weight")
        elif bmi >= 25 and bmi <= 29.9:
            print(f"{bmi} is overweight")
        elif bmi >= 30:
            print(f"{bmi} is obese")
    else:
        ("enter only positive values!!!!!!!") 
print(hello)

'''

while True:
    weight=float(input("enter the weight in kgs:"))
    height=float(input("enter the height in meters:"))
    try:
        if weight>0 and height>0:
             bmi=(weight)/((height)**2)
        print(f'bmi is:{bmi}')
        if bmi<18.5:
            print("under weight")
        elif bmi>=18.5 and bmi<=24.9:
            print("normal weight")
        elif bmi>=25 and bmi<=29.9:
            print("over weight")
        else:
            print("obesity")
        break
    except Exception as e:
        print(e)


