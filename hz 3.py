#Напишите программу, которая запрашивает у пользователя строку и определяет, является ли она анаграммой другой строки (содержит те же символы в другом порядке).
def anogr(text_11 , text_22):
    text_11 = list(text_11)
    text_22 = list(text_22)
    if sorted(text_11) == text_22:
        otvet = "да, они анаграммы"
    else:
        otvet = "нет, они не онаграммы"
        return otvet



text_1 = input("Введите первый текст: ")
text_2 = input("Введите второй текст: ")
ss= anogr(text_1 , text_2)
print(ss)