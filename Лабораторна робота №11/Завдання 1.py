import pandas as pd

# Початкові дані зі словника лабораторної №5 з додатковими характеристиками - "Місто" та "Середнія оцінка"
schools = {
    "Школа №1": ["школа", 450, "Київ", 8.7],
    "Технікум електроніки": ["технікум", 320, "Львів", 7.9],
    "Училище дизайну": ["училище", 210, "Одеса", 7.3],
    "Школа №7": ["школа", 390, "Київ", 8.1],
    "Технікум транспорту": ["технікум", 280, "Харків", 7.5],
    "Школа-гімназія №3": ["школа", 510, "Київ", 9.1],
}

# Перетворення словника на DataFrame
try:
    df = pd.DataFrame({
        "Назва закладу": list(schools.keys()),
        "Тип": [schools[name][0] for name in schools],
        "Учнів": [schools[name][1] for name in schools],
        "Місто": [schools[name][2] for name in schools],
        "Середня оцінка": [schools[name][3] for name in schools],
    })
    print("DataFrame успішно створено.\n")
except Exception as e:
    print(f"Помилка при створенні DataFrame: {e}")
    df = None
# Виведення словника
print("Вміст словника")
for name, data in schools.items():
    print(f"{name}: тип — {data[0]}, учнів — {data[1]}, Місто — {data[2]}, Середня оцінка — {data[3]}")
print()

print("DataFrame")
print(df)

# Перші 3 рядки
print("\nПерші 3 записи таблиці (df.head(3))")
print(df.head(3))

# Типи даних
print("\nТипи даних у кожному стовпці (df.dtypes)")
print(df.dtypes)

# Розмір таблиці
print("\nРозмір таблиці (кількість рядків і стовпців) — df.shape")
print(df.shape)

# Описова статистика
print("\nОписова статистика числових полів (df.describe())")
print(df.describe())

# новий стовпець
df["Коефіцієнт якості"] = df["Середня оцінка"] * (df["Учнів"] / 100)

print("\nDataFrame з доданим стовпцем 'Коефіцієнт якості'")
print(df)

# Фільтрація школи з кількістю учнів > 400
filtered = df[df["Учнів"] > 400]
print("\nНавчальні заклади з кількістю учнів більше ніж 400")
print(filtered)

# Сортування за середнім балом (спадання)
sorted_df = df.sort_values(by="Середня оцінка", ascending=False)
print("\nСортування закладів за середньою оцінкою (спадання)")
print(sorted_df)

# Групування за типом закладу + середній бал
grouped = df.groupby("Тип")["Середня оцінка"].mean()
print("\nСередня оцінка за типом навчального закладу")
print(grouped)

# Додаткова агрегація
agg_results = df.groupby("Тип").agg(
    {
        "Учнів": ["sum", "mean", "max"],
        "Середня оцінка": ["mean", "min", "max"],
    }
)

print("\nДодаткова агрегація ")
print(agg_results)
