# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print ("Введите трехзначное число:")
a = int(input())
result = (int(a%10)+int(a/100)+int((a%100)/10))
print (result)