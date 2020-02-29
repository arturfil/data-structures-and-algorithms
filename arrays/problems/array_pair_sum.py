# Array Pair sum
# This function returns two pairs that summed, equal the target
# For this example I'm going to be using the following
# list = [4,1,3,4,1,5,6,9]
# target = 7

# The way I would solve it is run two for loops & check if index i + index j
# - equal the target, if so return, save those values and iterate
# - once you found another return and show the four values ( in pairs)
def pair_sum(list, sum):
  pair_1 = []
  pair_2 = []
  for i in list:
    for j in list:
      if i + j == sum:
        if len(pair_1) == 0:
          pair_1.append(i)
          pair_1.append(j)
          print(pair_1)
        else: 
          pair_2.append(i)
          pair_2.append(j)
          print(pair_1)
          return


pair_sum([1,2,4,5,6,7,8,9,10,11,12,13,14,15], 12)