def get_unique_list_numbers() -> list[int]:
    from random import randint
    list_unique_numbers = [randint(-10, 10) for _ in range(15)]
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
