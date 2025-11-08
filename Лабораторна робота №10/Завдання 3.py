import matplotlib.pyplot as plt
# Дані
countries = ['Japan', 'Ukraine', 'United States', 'Canada', 'India']
population = [126633000, 44957458, 330226227, 37618495, 1389030312]
# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    population,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Set3.colors,
    textprops={'color': 'black', 'weight': 'bold'}
)
# Додаємо легенду збоку
plt.legend(
    wedges,
    countries,
    title="Країни",
    loc="center left",
    bbox_to_anchor=(0.8, -0.5, 1, 1)
)
# Заголовок
plt.title('Населення країн у 2019 році (Population, total)', fontsize=14)
plt.axis('equal')
plt.show()
