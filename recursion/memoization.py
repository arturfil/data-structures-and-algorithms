# Memoization is what the name implies, its memory, memory of results for some computations 
#   that have already been done and you don't have to re-do them
# This comes in handy when you are doing trees computation and transactions and you already know the value of a certain node
# This comes in handy because rather than making the same computation at a costly expense (2Logn for trees I believe) you can store
# Values in a table that allows you to return the value at Constant time

# Exmaple of memoization with the factorial functions

# First create a dictionary (look up table or object in javascript) 
# Then create the factorial function
factorial_memo = {}

def factorial(n):
  if n < 2:
    return 1
  
  if not n in factorial_memo:
    # Uncomment this print statement if you want to see how memoization works
    # print(f"Round {n}")
    factorial_memo[n] = n * factorial(n -1)

  return factorial_memo[n]

# Uncoment these print statements if you want to see how memoization works
# print(factorial(4))
# print(factorial(19))
print(factorial(25))

print(factorial_memo)