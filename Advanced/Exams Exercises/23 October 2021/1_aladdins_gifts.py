# Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine.
# He asks Genie for help to prepare the wedding presents.
# First, you will receive a sequence of integers representing the materials for every wedding present.
# After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
# Your task is to mix materials with magic levels so you can make presents, listed in the table below.
# Gift	Magic needed
# Gemstone	100 to 199
# Porcelain Sculpture	200 to 299
# Gold	300 to 399
# Diamond Jewellery	400 to 499
# To make a present, you should take the last integer of materials and sum it with the first magic level value.
# If the result is between or equal to the numbers described in the table above,
# you make the corresponding gift and remove both materials and magic value. Otherwise:
# •	If the product of the operation is under 100:
# o	And if it is an even number, double the materials, and triple the magic, then sum it again.
# o	And if it is an odd number, double the sum of the materials and the magic level.
# Then, check again if it is between or equal to any of the numbers in the table above.
# •	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2.
# Then, check again if it is between or equal to any of the numbers in the table above.
# •	If, however, the result is not between or equal to any of the numbers in the table above
# after performing the calculation, remove both the materials and the magic level.
# Stop crafting gifts when you are out of materials or magic level.
# You have succeeded in crafting the presents when you've crafted either one of the pairs
# - a gemstone and a sculpture or gold and jewellery.
# Input
# •	The first line of input will represent the values of materials - integers, separated by a single space
# •	On the second line, you will be given the magic levels - integers, separated by a single space
# Output
# •	On the first line - print whether you have succeeded in crafting the presents:
# o	"The wedding presents are made!"
# o	"Aladdin does not have enough wedding presents."
# •	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
# o	"Materials left: {material1}, {material2}, …"
# o	"Magic left: {magicValue1}, {magicValue2}, …
# •	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
# "{present1}: {amount}
# {present2}: {amount}
# …
# {presentN}: {amount}"
from collections import deque


def checking(magic, items):
    if 100 <= magic <= 199:
        items["Gemstone"] += 1
    elif 200 <= magic <= 299:
        items["Porcelain Sculpture"] += 1
    elif 300 <= magic <= 399:
        items["Gold"] += 1
    elif 400 <= magic <= 499:
        items["Diamond Jewellery"] += 1
    return items


materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
items = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}
while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()
    total = material + magic_level
    if total >= 500:
        total = total // 2
    elif total <= 99 and total % 2 == 0:
        total = material * 2 + magic_level * 3
    elif total <= 99:
        total *= 2
    checking(total, items)

if (items["Gemstone"] and items["Porcelain Sculpture"]) or \
        (items["Gold"] and items["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
for item, quantity in sorted(items.items(), key=lambda x: x[0]):
    if quantity > 0:
        print(f"{item}: {quantity}")
