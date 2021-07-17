# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.

def random_number(n):
    import random
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return random.randint(range_start, range_end)

# Так как, в условии задачи не указано, где должен быть размещен файл, 
# по умолчанию принимается, что он размещен в директории с файлом программы.

with open("20000.txt", "w") as f:
    f.write(str(random_number(20000)))
