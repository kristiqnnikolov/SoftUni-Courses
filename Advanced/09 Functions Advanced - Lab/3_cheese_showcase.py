# White a function called sorting_cheeses that receives keywords arguments:
# •	The key represents the name of the cheese
# •	The value is a list with quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind
# in descending order. If two or more cheeses have the same number of pieces, sort them by their names in
# ascending order (alphabetically). For each kind of cheese, return their pieces quantities in descending order.


def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ""
    for cheese, quantity in sorted_cheeses:
        result += cheese + '\n'
        sorted_quantity = sorted(quantity, reverse=True)
        result += "\n".join([str(x) for x in sorted_quantity]) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
