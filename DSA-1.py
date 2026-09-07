'''
bubble_sort

 def bubble_sort(arr):
     n = len(arr)
     for i in range(n):
         for j in range(0, n - i - 1):
             if arr[j] > arr[j + 1]:
                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
     return arr
arr = [12, 543, 23, 12, 54]
print(bubble_sort(arr))


selection_sort

 def selection_sort(arr):
     n = len(arr)
     for i in range(n):
         min_index = i
         for j in range(i + 1, n):
             if arr[j] < arr[min_index]:
                 min_index = j
         temp = arr[i]
         arr[i] = arr[min_index]
         arr[min_index] = temp
     return arr
 arr = [64, 25, 12, 22, 11]
 print(selection_sort(arr))

insertion_sort

def insertion_sort(arr):
    n =len(arr)
    for i in range(1,n):
        key = arr[i]
        j= i-1
        while j >= 0 and arr[j]>key:
            arr[j+1]= arr[j]
            j = j-1
        arr[j+1] = key
    return arr
arr=[-1,3,5,1,2]
print(insertion_sort(arr))


#merg_sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [4, 3, 5, 1, 2]
print(merge_sort(arr))



name = "Jaswanth"
age = 21
email_id = "jaswanthande98@gmail.com"
print(email_id[8:15])


email_id =['jaswanthande98@gmail.com','yaswanthpilla55@gmail.com','jahnavidungala23@gmail.com','charansai2003@gmail.com']
users= {}
for i in range (len(email_id)):
    users[i+1] = email_id[i]
print(users)

'''

email_id =['jaswanthande98@gmail.com','yaswanthpilla55@gmail.com','jahnavidungala23@gmail.com','charansai2003@gmail.com']
data = tuple(enumerate(email_id,1))
print(data)
