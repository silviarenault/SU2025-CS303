import random
import numpy as np
import time

name = "Silvia Renault de Castro"
blazerID = "silvia"

#(1): LINEAR SEARCH
def linear_search(arr, x):
    # code linear search
    i=0
    while i < len(arr)
        if arr[i]==x
            return i
    return -1 # return index of x, -1 if not found

#(2): BINARY SEARCH
def binary_search(arr, low, high, x):
    while low<=high
        mid=(low+high)/2
        if arr[mid]==x
            return mid
        elif arr[mid]<x
            low=mid+1
        else
            high=mid-1
    return -1 # return index of x, -1 if not found

#(3): TEST FUNCTIONS
'''
params:
    arr - randomly generated array
    keys - array of integers to search for in array
    
returns:
    returns an array of indices of each key's location, -1 if key is not found
'''
def linear_search_1000(arr, keys):
    ind=[]
    for i in keys:
        ind.append(linear_search(arr,keys))
    return ind
    return -1 # return an array of indices of each key

def binary_search_1000(arr, keys):
    # TODO: SORT THE ORIGINAL ARRAY (arr), DO NOT SET A NEW ARRAY EQUAL TO THE SORTED ARRAY
    for j in range(1, len(arr)):
        key=arr[j]
        i=j-1
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i=i-1
            arr[i+1]=key
    ind=[]
    for i in keys:
        ind.append(binary_search(arr,0,len(arr)-1,i))
    return ind
    return -1 # return an array of indices of each key

############# DO NOT MODIFY CODE BELOW THIS LINE #############

def gen_array(n):
    arr = np.zeros(n)
    for i in range(n):
        arr[i] = random.randint(0, n)
    return arr

print(f"Name: {name}")
print(f"BlazerID: {blazerID}")

print("------ Linear Search ------")
keys = gen_array(1000)
for n in range(4, 19):
    is_true = True
    arr = gen_array(2**n)

    start = time.time_ns()
    key_indices = linear_search_1000(arr, keys)
    stop = time.time_ns()

    for i in range(len(keys)):
        index = int(key_indices[i])
        if (index != -1) and (keys[i] != arr[index]):
            is_true = False
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")


print("------ Binary Search ------")
for n in range(4, 19):
    is_true = True
    arr = gen_array(2**n)

    start = time.time_ns()
    key_indices = binary_search_1000(arr, keys)
    stop = time.time_ns()

    if (n == 4):
        sorting = True
        sort_arr = np.sort(arr.copy())
        for i in range(len(arr)):
            if arr[i] != sort_arr[i]:
                sorting = False
        print(f"Sorting array check: {sorting}")

    for i in range(len(keys)):
        index = int(key_indices[i])
        if (index != -1) and (keys[i] != arr[index]):
            is_true = False
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")