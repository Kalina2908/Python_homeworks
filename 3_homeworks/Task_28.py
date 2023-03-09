# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4 

def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return a + sum(1, b-1)


print("Введите первое число:")
num_1 = int(input())
print("Введите второе число:")
num_2 = int(input())

print(f"Получем в результате: {sum(num_1, num_2)}")