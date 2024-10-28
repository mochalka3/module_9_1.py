def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        result = func(int_list)
        results[func.__name__] = result


    return results

int_list = [6, 20, 15, 9]

result1 = apply_all_func(int_list, max, min)
print(result1)  # {'max': 20, 'min': 6}

result2 = apply_all_func(int_list, len, sum, sorted)
print(result2)  # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
