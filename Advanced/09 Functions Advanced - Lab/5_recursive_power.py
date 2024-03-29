# Create a recursive function called recursive_power() which should receive a number and a power.
# Using recursion, return the result of number ** power. Submit only the function in the judge system.

def recursive_power(x, y):
    if y == 0:
        return 1
    return x * recursive_power(x, y - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
