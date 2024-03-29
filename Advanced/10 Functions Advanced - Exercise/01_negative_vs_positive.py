# You will receive a sequence of numbers (integers) separated by a single space.
# Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:
# •	On the first line, print the sum of the negatives
# •	On the second line, print the sum of the positives
# •	On the third line:
# o	If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# o	If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.
def negative_positive(*args):
    positive = 0
    negative = 0
    for x in args:
        if x > 0:
            positive += x
        else:
            negative -= -x
    if abs(negative) > positive:
        return print(negative, "\n", positive, "\n""The negatives are stronger than the positives")
    elif positive > abs(negative):
        return print(negative, "\n", positive, "\n""The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
negative_positive(*numbers)
