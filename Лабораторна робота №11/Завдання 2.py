import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_csv('comptagevelo2014.csv')
try:
    df = pd.read_csv('comptagevelo2014.csv')
    print("Файл відкрито")
except FileNotFoundError:
    print(f"\nФайл '{'comptagevelo2014.csv'}' не знайдено.")

# Перетворення дати
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)

# Перевірка датафрейму
print(df.head())
print("\nІнформація")
print(df.info())

print("\nОписова статистика")
print(df.describe())

# Загальна кількість велосипедистів за рік
numeric_cols = df.select_dtypes(include=['int64', 'float64'])
total_all = numeric_cols.sum().sum()

print("\n=== Загальна кількість велосипедистів за рік ===")
print(total_all)

# Загальна кількість за кожною велодоріжкою
total_each = numeric_cols.sum()

print("\nКількість велосипедистів на кожній доріжці")
print(total_each)

# Створення стовпця з місяцем
df['Month'] = df['Date'].dt.month

# Вибір трьох велодоріжок користувачем
print("\nДоступні велодоріжки:")
print(list(numeric_cols.columns))

chosen = input("\nВведіть три велодоріжки через кому: ").split(',')
chosen = [x.strip() for x in chosen]

# Перевірка наявності введених доріжок у даних
for lane in chosen:
    if lane not in numeric_cols.columns:
        print(f"Велодоріжка '{lane}' не знайдена в даних.")
        exit()

# Найпопулярніший місяць для обраних доріжок
popular_months = df.groupby('Month')[chosen].sum().idxmax()
print("\nНайпопулярніші місяці для обраних доріжок:")
print(popular_months)

# Графік завантаженості однієї доріжки по місяцях
lane = 'Berri1'
monthly = df.groupby('Month')[lane].sum()
plt.figure(figsize=(12, 6))
plt.plot(monthly, marker='o')
plt.title(f'Завантаженість велодоріжки {lane} по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.grid(True)
plt.tight_layout()
plt.show()
