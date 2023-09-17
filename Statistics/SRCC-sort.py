'''
SRCC-sort.py 
v1.0.0
nail_
'''

def Input_Numbers(arr):
    c = 0
    while c == 0:
        temp = float(input("Input number "))         
        arr.append(temp)
        if temp == 0.0:               
            c += 1
            arr.pop()
    return arr

def AssignRanks(arr):
    sorted_arr = sorted(arr) 
    ranks = {}

    for i in range(len(sorted_arr)):
        if i == 0 or sorted_arr[i] != sorted_arr[i-1]:
            ranks[sorted_arr[i]] = i + 1
        else:
            ranks[sorted_arr[i]] = (i + 1 + ranks[sorted_arr[i-1]]) / 2

    ranked_arr = [ranks[num] for num in arr]

    return ranked_arr

arr = []
arr = Input_Numbers(arr)
ranked_arr = AssignRanks(arr)

print("Unsorted:", arr)
print("Ranked:", ranked_arr)
