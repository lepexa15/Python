import math
# Перша функція
def expression(x):
    if x <= 0:
        print("x має бути додатним числом")
        return None
    z = (2 * math.tan(x) - math.sqrt(x)) / x
    return z
# Друга функція
def suma(x, y):
    totsum = 0
    start = min(x, y)
    end = max(x, y)
    for i in range(start, end + 1):
        if i % 3 == 0:
            totsum += i
    return totsum
# Обчислення виразу
xinput = float(input("Введіть число x: "))
resultz = expression(xinput)
if resultz is not None:
        print("Значення виразу z = ", resultz)
# Сума чисел, кратних 3
sum_x = int(input("Введіть від якого числа (x) знаходити суму: "))
sum_y = int(input("Введіть до якого числа (y) знаходити суму: "))
while sum_x > sum_y:
    print("y не може бути менше за x. Введіть числа ще раз.")
    sum_x = int(input("Введіть від якого числа (x): "))
    sum_y = int(input("Введіть до якого числа (y): "))
result_sum = suma(sum_x, sum_y)
print("Сума чисел, кратних 3, від х до у = ", result_sum)
