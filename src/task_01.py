import random


def find_min_max(array):
    if len(array) == 1:
        return array[0], array[0]
    if len(array) == 2:
        return min(array[0], array[1]), max(array[0], array[1])

    middle = len(array) // 2
    left_min, left_max = find_min_max(array[:middle])
    right_min, right_max = find_min_max(array[middle:])

    all_array_min = min(left_min, right_min)
    all_array_max = max(left_max, right_max)

    return (all_array_min, all_array_max)


def gen_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


generated_array = gen_array(100, 10, 1000000)
print(f"Generated Array: {generated_array}")
min, max = find_min_max(generated_array)
print(f"---------------------------------------")
print(f"Min: {min}, Max: {max}")
