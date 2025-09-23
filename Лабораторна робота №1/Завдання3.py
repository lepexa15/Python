#Завдання 3
n = int(input("Введіть ціле число N (1 < N < 9): "))
while n < 1 or n > 9:
    n = int(input("Умова порушена введіть коректне значення: "))
for i in range(1, n + 1):
    print("        ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

