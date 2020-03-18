# Buble sort algorithm
# We sort with this algorithm by running two for-loops where in each loop, you start from the beggining
# And then you compare index i against index i+1, if i > i+1 then switch values, else continue throughout the
# list.

# But, bubble sort is one of the least efficient sorts therefore is not advise to use it.

def bubble_sort(arr):
  for n in range(len(arr) - 1, 0, -1):
    for k in range(n):
      if arr[k] > arr[k+1]:
        temp = arr[k]
        arr[k] = arr[k+1]
        arr[k+1] = temp

  return arr

arr1 = [1,2,3,34,23,12,8]

print(bubble_sort(arr1))