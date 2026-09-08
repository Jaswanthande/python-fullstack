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
