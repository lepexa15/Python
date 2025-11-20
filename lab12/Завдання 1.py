import cv2
img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")
# Перевірка, чи зображення завантажені
if img1 is None or img2 is None:
    print("Помилка: не вдалося завантажити зображення.")
    exit()
# Привести до однакового розміру
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
# Перетворення в градації сірого
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# Різниця
diff = cv2.absdiff(gray1, gray2)
# Порогове перетворення
_, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
# Пошук контурів
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Копія зображення для малювання
output = img1.copy()
# Малюємо знайдені контури
for cnt in contours:
    if cv2.contourArea(cnt) > 50:  # відкидаємо дрібні шумові контури
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 2)
# Вивід
cv2.imshow("Difference", diff)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()