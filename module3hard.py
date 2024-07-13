data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    False,
    ((), False, [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    def recursive_sum(*elements):
        total = 0
        for element in elements:
            if isinstance(element, (list, tuple, set)):
                total += recursive_sum(*element)
            elif isinstance(element, dict):
                total += recursive_sum(*element.keys(), *element.values())
            elif isinstance(element, int):
                total += element
            elif isinstance(element, str):
                total += len(element)
        return total

    return recursive_sum(*args)


result = calculate_structure_sum(data_structure)
print(result)
