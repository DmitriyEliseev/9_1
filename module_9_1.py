def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        results[func.__name__] = func(int_list)

    return results

# Пример функций для тестирования
def my_min(lst):
    return min(lst)

def my_max(lst):
    return max(lst)

def my_len(lst):
    return len(lst)

def my_sum(lst):
    return sum(lst)

def my_sorted(lst):
    return sorted(lst)

# Пример использования функции apply_all_func
print(apply_all_func([6, 20, 15, 9], my_max, my_min))
print(apply_all_func([6, 20, 15, 9], my_len, my_sum, my_sorted))
