from math import log
from functools import cache

# Define a simple function
def square_input(x):
    return x*x

# define another function to call a function
def apply_function(func_x, input_x):
    return map(func_x, input_x)


a = [2, 3, 4]
print(apply_function(square_input, a))
print(apply_function(log, a))

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(15))
print(factorial.cache_info())
