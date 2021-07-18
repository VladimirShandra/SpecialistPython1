# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: все элементы списка должны быть гарантировано уникальными(неповторяющимися)
# Если создать список с заданными параметрами невозможно - функция должна выбросить исключение(любое)

def list_n_numbers(num_of_el, of, to):
    import random
    list_numbers = []
    for _ in range(num_of_el):
        list_numbers = random.sample(range(of, to), num_of_el)
    return list_numbers


number_of_elements = int(input("Укажите параметры списка.\nВведите количество элементов списка:"))

while True:  # Идет проверка на корректность указания диапазона
    print("Элементы будут в диапазоне:")
    a = int(input("от a:"))
    b = int(input("до b:"))
    try:
        if a > b:
            raise ValueError
        break
    except ValueError:
        print("Некорректно введен диапазон, a должно быть меньше b. Введите новые параметры")
try:
    print(f"Список состоит из следующих уникальных (не повторяющихся) элементов:",
          *list_n_numbers(number_of_elements, a, b))
except ValueError:
    print(f"Невозможно пострить список из {number_of_elements} уникальных (не повторяющихся) элементов"
          f" в дипазаоне от {a} до {b}")
