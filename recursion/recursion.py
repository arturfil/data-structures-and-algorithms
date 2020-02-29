# In this example I'm going to show how recursion works
# A very common use is using the factorial function:
  # - The factorial function thakes one parameter n and it will multilpy that vaue times (n - 1) 
  # until the remaining n = 1
# graphica example: 9! -> nine factorial 
  # 9! = 9 * 8! 
  # 9! = 9 * 8 * 7!
  # 9! = 9 * 8 * 7 * 6!
  # 9! = 9 * 8 * 7 * 6 * 5!
  # 9! = ...
  # ...
  # All the way where there is no more " ! " 
  # - after that you return the value 

def factorial(n):
  if n == 1:
    return n
  else:
    return n * factorial(n - 1)

# Uncomment to see example
# print(factorial(9))

# Another very popular example to explain recursion is the fibonacci sequence
# where the (fib n = 1) or (fib n = 2) = 1 and afer that is fib(n+1)
# Fibonacci sequence 1,1,2,3,5,8,13,21,34,55...
# This is because the mathematical formula is Fn = Fn-1 + Fn-2

# this is how we express that formula with a python function
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

print(fib(9))