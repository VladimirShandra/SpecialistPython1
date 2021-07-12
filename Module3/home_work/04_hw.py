# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

numbers = [2,-5,8,9,-25,25,4]
results = []
for el in numbers:
    if el > 0 and el**0.5%1==0:
        results.append(int(el**0.5))
print(results)
