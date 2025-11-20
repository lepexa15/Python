import cv2
import numpy as np

# Завантаження
img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")
if img1 is None or img2 is None:
    print("Помилка: не вдалося завантажити зображення.")
    exit()
# Приводимо до однакового розміру
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
# Різниця NumPy
difference = np.abs(img1.astype(int) - img2.astype(int))

#  Числові показники
print("===== Різниця (NumPy) =====")
print("Сума різниць:", np.sum(difference))
print("Середня різниця:", np.mean(difference))
print("Максимальна різниця:", np.max(difference))
