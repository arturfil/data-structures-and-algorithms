# Binary search has a 0(logn) time complexity which es fairly good.
# you can make a binary search with a for loop or you can make it recursively
# NOTE: for this to work, the array has te be previously sorted

def binary_search(arr, target):
    min = 0
    max = len(arr) - 1
    mid = 0
    round = 1
    while target != arr[mid]:
        mid = (max + min) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            max = mid
        else:
            min = mid
        print(f"This is round {round}")
        round += 1
    
# test array 
array_1 = []
for i in range(0,101):
    array_1.append(i)

print(array_1)
print(binary_search(array_1, 99))

# Revursive binary search

def binary_recursive_search(arr, target):

    if len(arr)== 0 or (len(arr) == 1 and arr[0] != target):
        return False

    mid = arr[len(arr)//2]

    if target == mid: 
        return True
    if target < mid: 
        return binary_recursive_search(arr[:len(arr)//2], target)
    if target > mid:
        return binary_recursive_search(arr[len(arr)//2+1:], target)

# Test array_2
array_2 = []
for i in range(0,101):
    array_2.append(i)

print(binary_recursive_search(array_2, 88))