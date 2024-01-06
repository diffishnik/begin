#Создайте функцию, которая принимает на вход список строк и возвращает новый список, содержащий только строки, состоящие из букв верхнего регистра.
def spisok(hz):
    spisok = list(spisok)
    spisok_0 = {}
    for char in spisok:
        if char.isalpha() and char.isup():
            spisok_0.get(char)
    return spisok_0


text = input("Vvedite text:  ")
otvet = spisok(text)
print(otvet)
