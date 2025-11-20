import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt
# Завантаження тексту
try:
    text = gutenberg.raw('chesterton-brown.txt')
except Exception as e:
    print(f"Помилка завантаження тексту: {e}")
    text = ""
# Токенізація
words = nltk.word_tokenize(text)
# Кількість слів
print("Кількість слів у тексті:", len(words))
# ТОП 10 слів
freq = FreqDist(words)
top10 = freq.most_common(10)
print("\n10 найбільш вживаних слів:")
for w, c in top10:
    print(w, ":", c)
plt.figure(figsize=(10,5))
plt.bar([w for w,_ in top10], [c for _,c in top10])
plt.title("ТОП-10 слів (без очищення)")
plt.show()
# 3. Очищення
stop_words = set(stopwords.words('english'))
cleaned_words = [
    w.lower() for w in words
    if w.isalpha() and w.lower() not in stop_words
]
freq_clean = FreqDist(cleaned_words)
top10_clean = freq_clean.most_common(10)
print("\n10 найбільш вживаних після очищення:")
for w, c in top10_clean:
    print(w, ":", c)
plt.figure(figsize=(10,5))
plt.bar([w for w,_ in top10_clean], [c for _,c in top10_clean])
plt.title("ТОП-10 слів після очищення")
plt.show()
