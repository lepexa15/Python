def print_all(schools):
    #Виведення всіх значень словника
    print("\nВміст словника:")
    for name, data in schools.items():
        print(f"{name}: тип — {data[0]}, кількість учнів — {data[1]}")
    print()
def add(schools):
    #Додавання нового запису у словник
    try:
        name = input("Введіть назву навчального закладу: ")
        if name in schools:
            print("Такий навчальний заклад вже існує")
            return
        type_ = input("Введіть тип закладу (школа / технікум / училище): ").strip().lower()
        students = int(input("Введіть кількість учнів: "))
        schools[name] = [type_, students]
        print(f"Додано: {name}.")
    except ValueError:
        print("кількість учнів має бути числом")
def delete(schools):
    #Видалення запису зі словника
    name = input("Введіть назву навчального закладу для видалення: ")
    try:
        del schools[name]
        print(f"Видалено {name}.")
    except KeyError:
        print("такого навчального закладу не існує")
def print_sorted(schools):
    #Виведення словника за відсортованими назвами
    print("\nСловник за алфавітом:")
    for name in sorted(schools.keys()):
        data = schools[name]
        print(f"{name}: тип — {data[0]}, кількість учнів — {data[1]}")
    print()
def total_students(schools):
    #загальна кількість учнів у школах
    total = sum(data[1] for data in schools.values() if data[0] == "школа")
    print(f"Загальна кількість учнів у школах: {total}\n")
def menu():
    #Головне меню
    print("МЕНЮ")
    print("1 – Вивести всі заклади")
    print("2 – Додати заклад")
    print("3 – Видалити заклад")
    print("4 – Вивести за відсортованими назвами")
    print("5 – Підрахувати кількість учнів у школах")
    print("0 – Вихід\n")
def main():
    #Початкові дані
    schools = {
        "Школа №1": ["школа", 450],
        "Технікум електроніки": ["технікум", 320],
        "Училище дизайну": ["училище", 210],
        "Школа №7": ["школа", 390],
        "Технікум транспорту": ["технікум", 280],
        "Школа-гімназія №3": ["школа", 510],
    }
    while True:
        menu()
        choice = input("Оберіть дію: ").strip()
        if choice == "1":
            print_all(schools)
        elif choice == "2":
            add(schools)
        elif choice == "3":
            delete(schools)
        elif choice == "4":
            print_sorted(schools)
        elif choice == "5":
            total_students(schools)
        elif choice == "0":
            print("Вихід з програми")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.\n")
main()
