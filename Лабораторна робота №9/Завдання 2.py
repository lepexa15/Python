import json
def load_data():
    #Завантаження даних з JSON файлу
    try:
        with open("schools.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return {}

def print_all(schools):
    #Виведення всіх записів
    if not schools:
        print("Файл порожній.\n")
        return
    print("\nВміст файлу:")
    for name, data in schools.items():
        print(f"{name}: тип — {data[0]}, кількість учнів — {data[1]}")
    print()

def add(schools):
    #Додавання нового запису
    try:
        name = input("Введіть назву навчального закладу: ")
        if name in schools:
            print("Такий навчальний заклад вже існує.")
            return
        type_ = input("Введіть тип (школа / технікум / училище): ").strip().lower()
        students = int(input("Введіть кількість учнів: "))
        schools[name] = [type_, students]
        with open("schools.json", "w", encoding="utf-8") as f:
            json.dump(schools, f, indent=4, ensure_ascii=False)
        print(f"Додано: {name}.\n")
    except ValueError:
        print("Помилка: кількість учнів має бути числом.\n")

def delete(schools):
    #Видалення запису
    name = input("Введіть назву навчального закладу для видалення: ")
    if name in schools:
        del schools[name]
        with open("schools.json", "w", encoding="utf-8") as f:
            json.dump(schools, f, indent=4, ensure_ascii=False)
        print(f"Видалено {name}.\n")
    else:
        print("Такого навчального закладу не існує.\n")

def search(schools):
    #Пошук за назвою або типом
    if not schools:
        print("Словник порожній.\n")
        return
    mode = input("Пошук за (1 - назвою, 2 - типом): ").strip()
    if mode == "1":
        name = input("Введіть назву закладу: ").strip()
        if name in schools:
            data = schools[name]
            print(f"{name}: тип — {data[0]}, кількість учнів — {data[1]}")
        else:
            print("Не знайдено.\n")
    elif mode == "2":
        type_ = input("Введіть тип (школа / технікум / училище): ").strip().lower()
        found = False
        for name, data in schools.items():
            if data[0] == type_:
                print(f"{name}: тип — {data[0]}, кількість учнів — {data[1]}")
                found = True
        if not found:
            print("Нічого не знайдено.\n")
    else:
        print("Невірний вибір.\n")

def print_sorted(schools):
    #Виведення відсортованих назв
    if not schools:
        print("Файл порожній.\n")
        return
    print("\nЗаклади за алфавітом:")
    for name in sorted(schools.keys()):
        data = schools[name]
        print(f"{name}: тип — {data[0]}, кількість учнів — {data[1]}")
    print()

def total_students(schools):
    #Обчислення загальної кількості учнів у школах і запис результату у файл
    total = sum(data[1] for data in schools.values() if data[0] == "школа")
    result = {"Загальна кількість учнів у школах": total}
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    print(f"Загальна кількість учнів у школах: {total}")
    print(f"Результат записано у файл '{"result.json"}'.\n")

def menu():
    print("=== МЕНЮ ===")
    print("1 – Вивести всі заклади")
    print("2 – Додати заклад")
    print("3 – Видалити заклад")
    print("4 – Пошук за полем")
    print("5 – Вивести за алфавітом")
    print("6 – Підрахувати кількість учнів у школах та записати у JSON")
    print("0 – Вихід\n")

def main():
    schools = {
  "Школа №1": [ "школа", 450 ],
  "Технікум електроніки": [ "технікум", 320 ],
  "Училище дизайну": [ "училище", 210 ],
  "Школа №7": [ "школа", 390 ],
  "Технікум транспорту": [ "технікум", 280 ],
  "Школа-гімназія №3": [ "школа", 510 ]
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
            search(schools)
        elif choice == "5":
            print_sorted(schools)
        elif choice == "6":
            total_students(schools)
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.\n")
main()
