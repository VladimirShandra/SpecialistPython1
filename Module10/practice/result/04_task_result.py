# Одноклеточная амеба каждые 3 часа делится на 2 такие же амёбы.
# Необходимо определить, сколько будет амеб через n часов, если первоначально была только одна амёба.
# Формат входных данных: Вводится целое положительное число n.
# Формат выходных данных: Требуется одно число — конечное число амеб.

n = int(input("Введите количество часов:"))

count_ameba = 2 ** (n // 3)

print("Через",n,"часов будет",count_ameba,"амеб")
