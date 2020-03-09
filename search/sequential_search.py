# not the most efficient search because there are various ways to do this quicker
# This will have a O(n) time complexity

def sequential_search(target, array):
    for i in range(0,len(array)):
        if array[i] == target:
            return array[i]

from random import randint

new_arr = [3,2,5,6,7,8,12,15,26]

print(new_arr)

print(sequential_search(6, new_arr))
