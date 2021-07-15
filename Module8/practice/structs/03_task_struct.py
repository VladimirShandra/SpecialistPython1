# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов


from random import randint

n = randint(0, 15)
random_list = [randint(-100, 100) for i in range(n)]


def num_counts(number_list):
    count = 0
    for el in number_list:
        if el < 10:
            count += 1
    return count

count_list = [el for el in random_list if el < 10]
sum_list = [el for el in random_list if el > 0]
average_list = [el for el in random_list if el % 2 == 0]
print("Список произвольных чисел:", random_list)
print("Количество элементов списка не превышающие 10:", num_counts(count_list))
print("Сумма всех положительных элементов списка:",sum(sum_list))
print("Список четных элементов:", average_list)
print("Среднее арифметическое всех четных элементов:",sum(average_list) / len(average_list))
