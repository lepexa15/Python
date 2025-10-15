#Завдання 3
def delete():

    A = list(map(int, input("Введіть список чисел через пробіл: ").split()))
    print("Початковий список:", A)

    result = []
    for i in range(len(A)):
        if i % 2 != 0:
            result.append(A[i])

    print("Список після видалення елементів із парними номерами:", result)
    return result

delete()