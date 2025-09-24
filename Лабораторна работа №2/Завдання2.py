from modul import suma
sum_x = int(input("Введіть від якого числа (x) знаходити суму: "))
sum_y = int(input("Введіть до якого числа (y) знаходити суму: "))

while sum_x > sum_y:
    print("y не може бути менше за x. Введіть числа ще раз.")
    sum_x = int(input("Введіть від якого числа (x): "))
    sum_y = int(input("Введіть до якого числа (y): "))
result_sum = suma(sum_x, sum_y)
print("Сума чисел, кратних 3, від х до у = ", result_sum)
