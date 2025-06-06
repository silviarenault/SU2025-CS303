import random
import numpy as np
import time

name = ""
blazerID = ""

#(1): LINEAR SEARCH
def linear_search(arr, x):
    # code linear search
    return -1 # return index of x, -1 if not found

#(2): BINARY SEARCH
def binary_search(arr, low, high, x):
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
    return -1 # return an array of indices of each key

def binary_search_1000(arr, keys):
    # TODO: SORT THE ORIGINAL ARRAY (arr), DO NOT SET A NEW ARRAY EQUAL TO THE SORTED ARRAY
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