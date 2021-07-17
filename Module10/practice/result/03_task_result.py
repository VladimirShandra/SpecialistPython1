# С некоторого момента прошло некоторое количество дней. Сколько полных недель прошло с этого же момента?
# Формат входных данных: Вводится целое положительное число — количество прошедших дней.
# Формат выходных данных: Выведите целое число недель.
# Уточнение: каждые 7 прошедших дней равны одной полной неделе.

def ending_weeks(number_weeks):
    if number_weeks % 10 == 1 and number_weeks != 11:
        return "неделя"
    elif 2 <= number_weeks % 10 <= 4 and number_weeks // 10 != 1:
        return "недели"
    else:
        return "недель"


number_of_days = int(input("Введите количество прошедших дней:"))

number_weeks = number_of_days // 7

print("С некоторого момнета прошло :", number_weeks, ending_weeks(number_weeks))
