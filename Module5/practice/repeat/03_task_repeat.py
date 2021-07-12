# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
def palindrome(number):
    return (str(number) == str(number)[::-1])
a = 123320
b = 123321
number=0
count=0
for i in range(a,b+1):
    number=i
    if palindrome(number)==True:
        count+=1
print(count)




