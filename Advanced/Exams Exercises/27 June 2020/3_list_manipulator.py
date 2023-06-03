# Write a function called list_manipulator which receives a list of numbers as first parameter and
# different amount of other parameters. The second parameter might be "add" or "remove".
# The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
# •	In case of "add" and "beginning", add the given numbers to the beginning
# of the given list of numbers and return the new list
# •	In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
# •	In case of "remove" and "beginning"
# o	If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
# o	If there are no other parameters, remove only the first element of the list.
# o	Finaly, return the new list
# •	In case of "remove" and "end"
# o	If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
# o	Otherwise if there are no other parameters, remove only the last element of the list.
# o	Finaly, return the new list
# For more clarifications, see the examples below.
# Input
# •	There will be no input
# •	Parameters will be passed to your function
# Output
# •	The function should return the new list of numbers
def list_manipulator(numbers, *args):
    nums = list(args[2:])
    if args[0] == 'add' and args[1] == 'beginning':
        for x in range(len(nums) - 1, -1, -1):
            numbers.insert(0, nums[x])
    elif args[0] == 'add' and args[1] == 'end':
        for x in range(len(nums)):
            numbers.append(nums[x])
    elif args[0] == 'remove' and args[1] == 'beginning':
        if len(args) == 2:
            numbers.pop(0)
        else:
            index = args[2]
            for x in range(index):
                numbers.pop(0)
    elif args[0] == 'remove' and args[1] == 'end':
        if len(args) == 2:
            numbers.pop()
        else:
            index = args[2]
            for x in range(index):
                numbers.pop()
    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
