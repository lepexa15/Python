import matplotlib.pyplot as plt
plt.title('Середньодобова температура за тиждень')
a = [14, 12, 15, 12, 9, 10, 7]
day = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
plt.xlabel('Дні тижня', color = 'gray')
plt.ylabel('Середньодобова температура', color = 'gray')
plt.grid(True)
plt.plot(day, a, 'blue')
plt.show()
