#Напишите программу, которая запрашивает у пользователя текст и определяет, какая буква встречается в тексте наибольшее количество раз. Выведите эту букву и количество ее вхождений.
def func(hz):
    list_1 = hz.lower()
   # Инициализация словаря для подсчета вхождений каждой буквы
    letter_count = {}

    # Подсчет вхождений каждой буквы в тексте
    for char in list_1:
        if char.isalpha():  # Учитываем только буквы
            letter_count[char] = letter_count.get(char, 0) + 1

    # Находим букву с максимальным количеством вхождений
    most_common_letter = max(letter_count, key=letter_count.get)
    return most_common_letter

def func1(hz):
    list_1 = hz.lower()
   # Инициализация словаря для подсчета вхождений каждой буквы
    letter_count = {}

    # Подсчет вхождений каждой буквы в тексте
    for char in list_1:
        if char.isalpha():  # Учитываем только буквы
            letter_count[char] = letter_count.get(char, 0) + 1

    # Находим букву с максимальным количеством вхождений
    most_common_letter = max(letter_count, key=letter_count.get)
    count_of_most_common_letter = letter_count[most_common_letter]
    return count_of_most_common_letter

text = input()
result = func(text)
result1 = func1(text)
print(f"Наибольшее количество раз встречается: {result}, повторяется она {result1} раз.")