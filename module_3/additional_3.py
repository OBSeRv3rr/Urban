def calculate_structure_sum(data_structure):
    def recursive_sum(element):
        total = 0
        if isinstance(element, int):
            total += element
        elif isinstance(element, str):
            total += len(element)
        elif isinstance(element, dict):
            for key, value in element.items():
                total += recursive_sum(key)
                total += recursive_sum(value)
        elif isinstance(element, (list, tuple, set)):
            for item in element:
                total += recursive_sum(item)
        return total

    return recursive_sum(data_structure)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
