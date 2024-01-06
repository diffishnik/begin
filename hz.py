#Создайте функцию, которая принимает на вход два списка чисел и возвращает новый список, содержащий только общие элементы этих списков.
def spisok(r1, r2):
    r1 = list(r1)
    r2 = list(r2)
    obs = {}
    for char_1 in r1:
        for char_2 in r2:
            if char_1 == char_2:
                obs.get(char_1)
    return obs



r = input("Write words:  ")
m = input("Write words:  ")
otvet = spisok(r, m)
print(f"Общие элементы: {otvet} ")