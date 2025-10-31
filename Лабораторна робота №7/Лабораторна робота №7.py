def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
    except Exception as e:
        print("Файл", file_name, "не відкрився:", e)
        return None
    else:
        print("Файл", file_name, "успішно відкрито")
        return file
# Імена файлів
file1_name = "TF13_1.txt"
file2_name = "TF13_2.txt"
# a)створення текстового файлу TF13_1
file_1_w = Open(file1_name, "w")
if(file_1_w != None):
    file_1_w.write("Programming - is cool! "
                   "Apple and orange, umbrella over island. "
                   "Open the file immediately!" )
    print("Інформацію успішно записано у TF13_1.txt")
    file_1_w.close()
    print("Файл TF13_1.txt закрито")
# б)пошук слів, які починаються з голосної
letters = "AEIOUYaeiouyАЕЄИІЇОУЮЯаеєиіїоуюя"
file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")
if file_2_r != None or file_2_w != None:
    text = file_2_r.read()
    # замінюємо розділові знаки на пробіли
    for ch in ",.!?;:-":
        text = text.replace(ch, " ")
    # розділяємо на слова
    words = text.split()
    for word in words:
        if len(word) > 0 and word[0] in letters:
            file_2_w.write(word + "\n")
    file_2_r.close()
    file_2_w.close()
    print("Файли TF13_1.txt і TF13_2.txt оброблені та закриті")
# в)виведення вмісту TF13_2.txt
print("\nСлова, які починаються з голосної (з TF13_2.txt):")
file_3_r = Open(file2_name, "r")
if(file_1_w != None):
    for line in file_3_r:
        print(line.strip())
    print("Файл TF13_2.txt закрито!")
    file_3_r.close()