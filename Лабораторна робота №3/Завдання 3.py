#Завдання 3

# Речення від користувача.
z = str(input("Введіть речення: "))

# Розділення речення на слова
words = z.split()

# Пошук найдовшого слова
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

# Виведення результату
print("Найдовше слово в реченні:", longest)
