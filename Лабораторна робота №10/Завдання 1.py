import matplotlib.pyplot as plt
import numpy as np

# Створення масиву значень x від 0.1 до 10 (0.1, щоб уникнути ділення на 0)
x = np.linspace(0.1, 10, 500)

# Обчислення значення функції F(x)
y = -5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

# Побудова графіка
plt.plot(x, y, label='F(x) = -5*cos(10x)*sin(3x)/x^(1/2)', color='green', linewidth=2)

# Додавання підписів та сітки
plt.title('Графік функції F(x)', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('F(x)', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()
