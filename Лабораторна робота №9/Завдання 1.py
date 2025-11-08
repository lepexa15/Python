import csv

flag = False  # прапорець для перевірки, чи знайдено країни

# Відкриваємо файл і виводимо Population, total за 2019 рік
try:
    with open("Data.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        print("Country Name: Population, total (2019)\n")

        # Перебираємо всі рядки у файлі
        for row in reader:
            if row.get("Series Name") == "Population, total" and row.get("2019 [YR2019]"):
                print(row["Country Name"], ":", row["2019 [YR2019]"])

except FileNotFoundError:
    print("Помилка: файл Data.csv не знайдено!")
    exit()
except Exception as e:
    print("Помилка при читанні файлу:", e)
    exit()

# Повторно відкриваємо файл для пошуку введених користувачем країн
try:
    with open("Data.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        countries = input("\nВведіть назви країн через кому: ").split(",")
        countries = [c.strip() for c in countries]
        print("Результати пошуку:\nCountry Name: Population, total (2019)\n")
        # Створюємо новий CSV для запису знайдених країн
        with open("result.csv", "w", newline="", encoding="utf-8") as outcsv:
            writer = csv.writer(outcsv, delimiter=";")
            writer.writerow(["Country Name", "2019"])

            for row in reader:
                if (
                    row.get("Series Name") == "Population, total"
                    and row.get("2019 [YR2019]")
                    and row["Country Name"] in countries
                ):
                    flag = True
                    print(row["Country Name"], ":", row["2019 [YR2019]"])
                    writer.writerow([row["Country Name"], row["2019 [YR2019]"]])

        # Якщо жодна країна не знайдена
        if not flag:
            print("Жодну з введених країн не знайдено у файлі.")

        else:
            print(f"\nРезультати записано у файл {"result.csv"}")

except FileNotFoundError:
    print("Помилка: файл Data.csv не знайдено!")
except Exception as e:
    print("Помилка при обробці файлу:", e)