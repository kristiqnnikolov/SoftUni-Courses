# Merry has a guinea pig named Puppy, that she loves very much.
# Every month she goes to the nearest pet store and buys him everything he needs – food, hay, and cover.
# On the first three lines, you will receive the quantity of food, hay, and cover,
# which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.
# Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet,
# then gives it a certain amount of hay equal to 5% of the rest of the food.
# On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
# Calculate whether the quantity of food, hay, and cover, will be enough for a month.
# If Merry runs out of food, hay, or cover, stop the program!


food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
for day in range(1, 31):
    food -= 0.300
    if day % 2 == 0:
        hay -= (food / 20)
    if day % 3 == 0:
        cover -= (weight / 3)
if food > 0 and hay > 0 and cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print(f"Merry must go to the pet store!")
