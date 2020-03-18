def insertion_sort(arr):
   # traverse through index 0 to len(arr)
  for i in range(1, len(arr)):

    current_value = arr[i]
    position = i

    while position > 0 and arr[position - 1]>current_value:
      arr[position] = arr[position-1]
      position = position - 1
    arr[position] = current_value


# testing algorithm
arr_1 = [5,2,7,99,22,33,66,32,11,22]
print(f"Unsorted array {arr_1}")
insertion_sort(arr_1)
print(f"\nSorted array {arr_1}")
