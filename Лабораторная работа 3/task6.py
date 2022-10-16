list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_ = list_numbers[max_index]

for i, current_value in enumerate(list_numbers):
    max_ = list_numbers[max_index]
    if current_value > max_:
        max_index = i
        current_value = list_numbers[max_index]
list_numbers[-1], list_numbers[max_index] = list_numbers[max_index],  list_numbers[-1]
print(list_numbers)
