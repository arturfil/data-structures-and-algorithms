# You have lists "normal arrays" [1,2,3]
# You have tuples (1,2,3)
# You have Strings which are ch char[] 

# Mermory of computer is stored in bits -> 8 bits = 1 byte
# When you create lists you can change reference to objects, (Like POINTERS!)

# Dynamic arrays, arrays in python are dynamic! DUH!

# Demostrantion of how a dynamic array works from the python language

### Lecture 1 ###
import sys
# set n
n = 10
data = []

for i in range(n):
  # Number of elements
  a = len(data)
  # Actual syze in bytes
  b = sys.getsizeof(data)

  print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a,b))
  #increase length by one
  data.append(n)