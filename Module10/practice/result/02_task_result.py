# На числовой прямой расположены точки A, B, C и D.
# Напишите программу, которая выведет, во сколько раз отрезок AB больше или меньше, чем отрезок CD.
# Формат входных данных:
# На вход программе подается четыре целых числа A, B, C и D.
# Расположение точек относительно друг друга на координатной прямой произвольное.
# Формат выходных данных:
# Выведите, во сколько раз отрезок AB больше, чем отрезок CD. Ответ введите с точностью до 6-ти знаков после запятой.


def ending(x):
    if 2 <= x % 10 <= 4 and x // 10 != 1:
        return "раза"
    return "раз"


print("Введите четыре точки:")
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

AB = abs(A - B)
CD = abs(C - D)

if AB >= CD and CD != 0:
    res = AB / CD
    if res == 1:
        print("Отрезок AB равен отрезку CD")
    else:
        print(f"Отрезок AB больше, чем отрезок CD в: {res:.6f}", ending(res))
elif AB <= CD and AB != 0:
    res = CD / AB
    if res == 1:
        print("Отрезок AB равен отрезку CD")
    else:
        print(f"Отрезок AB меньше, чем отрезок CD в: {res:.6f}", ending(res))
else:
    print("Длина каждого отрезка равна 0")
