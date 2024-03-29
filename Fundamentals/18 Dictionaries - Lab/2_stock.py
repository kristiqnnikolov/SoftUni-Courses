# After you have completed your first task, your boss decides to give you another one right away.
# Now not only you have to keep track of the stock, but also you should answer customers if
# you have some products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".

food = input().split()
result = {}
for key in range(0, len(food), 2):
    product = food[key]
    quantity = food[key + 1]
    result[product] = int(quantity)
wanted_list = input().split()

for key in wanted_list:
    if key in result:
        print(f"We have {result[key]} of {key} left")
    else:
        print(f"Sorry, we don't have {key}")
