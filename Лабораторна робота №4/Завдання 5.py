#Завдання 5
def search():
    A = input("Введіть текст (латинські літери): ")

    # Формуємо множину малих латинських літер, що входять у текст
    letters = {ch for ch in A if 'a' <= ch <= 'z'}
    print("Множина літер у тексті:", letters)

    # Визначаємо кількість розділових знаків
    punctuation = {'.', ',', '!', '?', ':', ';', '-', '(', ')', '"', "'"}
    count = sum(1 for ch in A if ch in punctuation)

    print("Кількість розділових знаків у тексті:", count)
    return letters, count

search()