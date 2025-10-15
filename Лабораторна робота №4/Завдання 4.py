#Завдання 4
def reverse():
    A = list(map(int, input("Введіть список чисел через пробіл: ").split()))
    print("Початковий список:", A)
    # Перестановка елементів у зворотному порядку
    reversed = A[::-1]
    print("Список у зворотному порядку:", reversed)
    return reversed
reverse()
