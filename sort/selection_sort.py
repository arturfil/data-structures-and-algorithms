# Selection sort is more efficient compared to bubble sort because
# it sorts a portion of the array and that portion doesn't have to be 
# re-adjusted ever again, therefore this yields more efficiency compared to 
# the one of the bubble sort.

def selection_sort(arr):
  for i in range(len(arr)):
    min_indx = i
    for j in range(i+1, len(arr)):
      if arr[min_indx] > arr[j]:
        min_indx = j
    
    # you can do it this way
    temp = arr[i]
    arr[i] = arr[min_indx]
    arr[min_indx] = temp

    # or a faster alternative is this way
    # arr[i], arr[min_indx] = arr[min_indx], arr[i]

  return arr

arr_1 = [3,34,23,12,95,21]
  
print(selection_sort(arr_1))