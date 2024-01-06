#Напишите программу, которая принимает на вход список чисел и выводит только уникальные числа, упорядоченные по возрастанию.
def unique_sorted_numbers(input_list):

    unique_numbers_set = set(input_list)


    sorted_unique_numbers = sorted(list(unique_numbers_set))

    return sorted_unique_numbers


input_numbers = [5, 2, 8, 2, 1, 5, 9, 8, 3]
result = unique_sorted_numbers(input_numbers)

print("Уникальные числа по возрастанию:", result)
