# Write a function called operate that receives an operator ("+", "-", "*" or "/")
# as first argument and multiple numbers (integers) as additional arguments (*args).
# The function should return the result of the operator applied to all the numbers.
# For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division
from functools import reduce


def operate(sign, *args):
    if sign == "+":
        return reduce(lambda x, y: x + y, args)
    elif sign == "-":
        return reduce(lambda x, y: x - y, args)
    elif sign == "*":
        return reduce(lambda x, y: x * y, args)
    elif sign == "/":
        return reduce(lambda x, y: x / y, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
