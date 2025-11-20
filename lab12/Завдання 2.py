import cv2
from skimage.metrics import structural_similarity as ssim
import os

# Завантаження медичного зображення з перевіркою існування
def load_image(filename):
    try:
        path = os.path.join(os.getcwd(), filename)
        img = cv2.imread(path)
        if img is None:
            raise FileNotFoundError(
                f"Файл '{filename}' не знайдено або формат не підтримується.\n"
                "Використовуйте знімки у форматах PNG, JPG або JPEG."
            )
        return img
    except Exception as e:
        print(f"Помилка завантаження '{filename}': {e}")
        return None

# Порівняння двох знімків методом SSIM
def compare_images(img1, img2):
    # Вирівнюємо розмір контрольного знімка
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    # Конвертація у відтінки сірого
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # Розрахунок SSIM та отримання карти різниць
    score, diff = ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype("uint8")
    # Бінарна маска патологій методом Оцу
    mask = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return score, diff, mask

# Створення папки для результатів та збереження файлів
def save_results(score, diff, mask):

    result_dir = "lung_results"
    os.makedirs(result_dir, exist_ok=True)

    cv2.imwrite(os.path.join(result_dir, "difference_lungs.png"), diff)
    cv2.imwrite(os.path.join(result_dir, "mask_lungs.png"), mask)

    # Текстовий звіт
    with open(os.path.join(result_dir, "lung_report.txt"), "w", encoding="utf-8") as f:
        f.write("ПОРІВНЯННЯ ЛЕГЕНЕВИХ ЗНІМКІВ (рентген/КТ)\n")
        f.write("-----------------------------------------\n")
        f.write(f"Ступінь структурної схожості (SSIM): {score * 100:.2f}%\n")
        f.write("Файли результатів:\n")
        f.write(" - difference_lungs.png (карта структурних змін)\n")
        f.write(" - mask_lungs.png (бінарна маска патологій)\n")

    print("\nРезультати збережено у папці 'lung_results/'")
    print("   → difference_lungs.png")
    print("   → mask_lungs.png")
    print("   → lung_report.txt")

# Головна функція
def main():
    print("==============================================")
    print("   АНАЛІЗ ЛЕГЕНЕВИХ ЗНІМКІВ (РЕНТГЕН / КТ)")
    print("==============================================")
    print("Введіть назви двох файлів у поточній директорії.")
    print("ПЕРШЕ зображення — попередній стан.")
    print("ДРУГЕ зображення — новий знімок.")
    print(f"Поточна папка: {os.getcwd()}\n")

    file1 = input("Назва першого знімка: ")
    file2 = input("Назва другого (нового) знімка: ")

    img1 = load_image(file1)
    img2 = load_image(file2)
    if img1 is None or img2 is None:
        print("не вдалося завантажити зображення.")
        return
    if img1 is None or img2 is None:
        print("неможливо завантажити зображення.")
        return
    print("\nВиконується аналіз легеневих знімків...")
    score, diff, mask = compare_images(img1, img2)
    print(f"\nСХОЖІСТЬ ЗНІМКІВ: {score * 100:.2f}%")
    if score < 0.80:
        print("Можливі значні структурні зміни у легенях.")
    elif score < 0.95:
        print("Виявлено помірні зміни.")
    else:
        print("Знімки майже ідентичні.")
    save_results(score, diff, mask)
# Запуск програми
main()
