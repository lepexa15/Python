#Завдання 2
# Задане слово
word = "програмування".lower()

# Слово, яке вводить користувач
user_word = input("Введіть слово для перевірки: ").lower()

# Перевірка
letters_exist = True

for letter in user_word:
    if letter not in word:
        letters_exist = False
        break

if letters_exist:
    print("у заданому слові є всі букви зі слова 'програмування'")
else:
    print("у заданому слові немає всіх букв зі слова 'програмування'")