# Пользователь Василий очень часто злоупотребляет восклицательными знаками!
# Напишите программу, которая будет заменять восклицательные знаки на точки.
# Пример строки: «Вася самый умный! Вася лучше всех! И ждет его успех! Вот так!»

text = input("Введите текст строки:")

dots=text.replace('!','.')

print(dots)

# Важно! Ваше решение должно работать не только с данной строкой, но и слюбой другой.
# Проверьте это, заменив текст примера на любой другой.
