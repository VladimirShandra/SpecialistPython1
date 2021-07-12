# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    num = str(ticket_number)
    sum_first_num = int(num[:1]) + int(num[1:2])
    sum_last_num = int(num[-1]) + int(num[-2])
    return sum_first_num == sum_last_num

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
