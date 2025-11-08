import matplotlib.pyplot as plt
import numpy as np

# Дані для Австралії
years_au = np.array([2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
internet_au = np.array([69.5, 71.7, 74.3, 76.0, 79.5, 79.0, 83.5, 84.0, 84.6, 86.5, 86.5])

#  Дані для України
years_ua = np.array([2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
internet_ua = np.array([17.9, 23.3, 28.7, 35.3, 41.0, 46.2, 48.9, 53.0, 58.9])

# Лінійний графік динаміки показника для двох країн
plt.figure(figsize=(8, 5))
plt.plot(years_au, internet_au, label='Australia', color='orange', marker='o')
plt.plot(years_ua, internet_ua, label='Ukraine', color='blue', marker='s')

plt.title('Internet users (per 100 people)', fontsize=15)
plt.xlabel('Year', fontsize=12, color='red')
plt.ylabel('Percentage of Internet Users', fontsize=12, color='red')
plt.legend()
plt.grid(True)
plt.show()

# Стовпчаста діаграма (вибір країни користувачем)
country = input("Введіть назву країни (Australia або Ukraine): ")

if country.lower() == "australia":
    plt.bar(years_au, internet_au, color='orange')
    plt.title('Internet users in Australia (per 100 people)', fontsize=14)
    plt.xlabel('Year', fontsize=12, color='red')
    plt.ylabel('Users per 100 people', fontsize=12, color='red')

elif country.lower() == "ukraine":
    plt.bar(years_ua, internet_ua, color='blue')
    plt.title('Internet users in Ukraine (per 100 people)', fontsize=14)
    plt.xlabel('Year', fontsize=12, color='red')
    plt.ylabel('Users per 100 people', fontsize=12, color='red')

else:
    print("Невідома країна. Спробуйте ще раз (Australia або Ukraine).")
    exit()

plt.grid(True)
plt.show()