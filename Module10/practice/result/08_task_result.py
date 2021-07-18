# Прочитав число из файла задачи 7, определите:
# Какие цифры встречаются в числе чаще всего?
# Если несколько цифр встречаются одинаковое максимальное кол-во раз - найдите любые.
# Является ли данное число(20000-значное) четным?


digit_count = {}

f = open("20000.txt", "r") # Так как в условии задачине указана директория где размещен файл, 
                           # по умолчанию файл размещен в директории с файлом программы

# 1. Какие цифры встречаются в числе чаще всего?
for line in f:
    digit_count = {digit: line.count(digit) for digit in line}

    sorted_dict = {k: digit_count[k] for k in sorted(digit_count, key=digit_count.get, reverse=True)}
    print(
        "Чаще всего встречаются цифры:\n" + "\n".join("{!r}: {!r},".format(k, v) for k, v in sorted_dict.items()) + "")

    # 2. Если несколько цифр встречаются одинаковое максимальное кол-во раз - найдите любые.
    max_count_digit = max(digit_count.values())
    print(f"Цифра {list(digit_count.keys())[list(digit_count.values()).index(max_count_digit)]} "
          f"встречается {max_count_digit} раз")

# 3. Является ли данное число(20000-значное) четным?

if int(line[-1]) % 2 == 0:
    print(f"Данное число({len(line)}-значное) является четным, так как оно заканчивается на {line[-1]}")
else:
    print(f"Данное число({len(line)}-значное) является нечетным, так как оно заканчивается на {line[-1]}")

f.close()
