#Создайте функцию, которая принимает на вход список строк и возвращает новый список, содержащий только строки, состоящие из букв верхнего регистра.
def vr(list):
    words=[]
    for i in list:
        if i.isupper():
            words.append(i)
    return words        
words2= input()
print(vr(words2))