#Завдання 1
a = int(input ("Введіть додатнє а: "))
while (a < 1 or a > 100):
    a = int(input ("Введіть ще раз а: "))
b = int(input ("Введіть b: "))
while (b < 1 or b > 100):
    b = int(input ("Введіть ще раз b: "))
if a > b:
    x = a / b + 31
elif a == b:
    x = -25
else:
    x = (a * 5 - 1) / a
print("Результат обчислення виразу: " , x)