#Завдання 2
n = 7

a = [[(i + j + 1) if (i + j < n) else 0 for j in range(n)] for i in range(n)]

for row in a:
    print(*row)