def get_count_char(str_):
  letters_dict = {}
  str_ = str_.lower()

  for letter in str_:
        if letter.isalpha():
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1

  return letters_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def count_percent(letters_dict):
    sum_ = sum(letters_dict.values())
    for letter in letters_dict:
        letters_dict[letter] = round(letters_dict[letter] / sum_ * 100, 2)
    return letters_dict
print(count_percent(get_count_char(main_str)))