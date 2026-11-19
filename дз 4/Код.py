import numpy as np
import pandas as pd


# ЗАГРУЗКА ДАННЫХ (Titanic dataset со столбцом Survived)
#
# При наличии локального файла train.csv можно заменить url на "train.csv"
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Проверка наличия обязательных столбцов
required_cols = ["Age", "Sex", "Pclass", "Fare", "Embarked", "Cabin", "Survived"]
assert all(col in df.columns for col in required_cols), "Отсутствуют обязательные столбцы!"


# ЧАСТЬ II. Загрузка и первичный анализ данных

# 7. Вывод первых n строк таблицы, где n вводится пользователем
try:
    n_str = input("Введите количество первых строк для вывода (n) [по умолчанию 5]: ")
    n = int(n_str) if n_str.strip() else 5
except ValueError:
    n = 5
print(f"\n7. Первые {n} строк таблицы:")
print(df.head(n))

# 8. Вывод последних 5 строк
print("\n8. Последние 5 строк таблицы:")
print(df.tail(5))

# 9. Общее количество строк и столбцов
print(f"\n9. Размер таблицы: {df.shape[0]} строк, {df.shape[1]} столбцов.")

# 10. Названия всех столбцов
print("\n10. Названия столбцов:", df.columns.tolist())

# 11. Типы данных каждого столбца
print("\n11. Типы данных столбцов:")
print(df.dtypes)

# 12. Разделение признаков на числовые и категориальные по смыслу данных
numeric_cols = ["Age", "Fare", "SibSp", "Parch"]
categorical_cols = ["Pclass", "Sex", "Embarked", "Cabin", "Survived"]
print("\n12. Числовые признаки:", numeric_cols)
print("    Категориальные признаки:", categorical_cols)

# 13. Среднее, медиана, минимум, максимум и стандартное отклонение числовых признаков
print("\n13. Статистика числовых признаков:")
print(df[numeric_cols].agg(["mean", "median", "min", "max", "std"]).T.round(2))

# 14. Количество пассажиров каждого класса (Pclass)
print("\n14. Количество пассажиров каждого класса (Pclass):")
print(df["Pclass"].value_counts().sort_index())

# 15. Количество уникальных значений в Embarked
print("\n15. Количество уникальных значений в Embarked:", df["Embarked"].nunique())



# ЧАСТЬ III. Обработка пропущенных значений

# 16. Количество пропусков в каждом столбце
missing_count = df.isnull().sum()
print("\n16. Количество пропусков в каждом столбце:")
print(missing_count)

# 17. Процент пропусков относительно общего числа строк
missing_percent = (df.isnull().mean() * 100).round(2)
print("\n17. Процент пропусков (%):")
print(missing_percent)

# 18. Столбец с максимальным количеством пропусков
print(f"\n18. Столбец с максимальным количеством пропусков: {missing_count.idxmax()} ({missing_count.max()})")

# 19. Характеристики Age ДО заполнения пропусков
age_before = {
    "Среднее арифметическое": df["Age"].mean(),
    "Медиана": df["Age"].median(),
    "Минимальный возраст": df["Age"].min(),
    "Максимальный возраст": df["Age"].max(),
    "Стандартное отклонение": df["Age"].std(),
    "Количество известных значений": df["Age"].count(),
}
orig_shape = df.shape

# 20. Заполнение пропусков в Age медианой
df["Age"] = df["Age"].fillna(df["Age"].median())

# 21. Повторный расчёт характеристик Age ПОСЛЕ заполнения
age_after = {
    "Среднее арифметическое": df["Age"].mean(),
    "Медиана": df["Age"].median(),
    "Минимальный возраст": df["Age"].min(),
    "Максимальный возраст": df["Age"].max(),
    "Стандартное отклонение": df["Age"].std(),
    "Количество известных значений": df["Age"].count(),
}

# 22. Таблица сравнения «до / после»
comparison_table = pd.DataFrame({"До обработки": age_before, "После обработки": age_after})
print("\n22. Сравнение характеристик возраста до и после обработки:")
print(comparison_table.round(2))

# 23. Удаление строк с отсутствующим Embarked
df = df.dropna(subset=["Embarked"])

# 24. Доля пропусков в Cabin; если > 50%, удалить столбец
cabin_missing_share = df["Cabin"].isnull().mean()
if cabin_missing_share > 0.5:
    df = df.drop(columns=["Cabin"])
    print(f"\n24. Столбец Cabin удалён (доля пропусков: {cabin_missing_share * 100:.2f}% > 50%).")

# 25. Проверка оставшихся пропусков
print("\n25. Оставшиеся пропуски после обработки:")
print(df.isnull().sum())

# 26. Сравнение количества строк и столбцов до и после обработки
print(f"\n26. Размер до обработки: {orig_shape}, после обработки: {df.shape}")



# ЧАСТЬ IV. Анализ данных с помощью NumPy

survived_np = df["Survived"].to_numpy()
sex_np = df["Sex"].to_numpy()
age_np = df["Age"].to_numpy()
fare_np = df["Fare"].to_numpy()

# 31. Общий процент выживших
overall_surv = np.mean(survived_np == 1) * 100

# 32. Процент выживших отдельно среди мужчин и женщин
male_mask = sex_np == "male"
female_mask = sex_np == "female"
male_surv = np.mean(survived_np[male_mask] == 1) * 100
female_surv = np.mean(survived_np[female_mask] == 1) * 100

# 33. Средний возраст мужчин и женщин
male_age = np.mean(age_np[male_mask])
female_age = np.mean(age_np[female_mask])

# 34. Средний возраст выживших и погибших отдельно для мужчин и женщин
surv_mask = survived_np == 1
dead_mask = survived_np == 0
male_surv_age = np.mean(age_np[male_mask & surv_mask])
male_dead_age = np.mean(age_np[male_mask & dead_mask])
female_surv_age = np.mean(age_np[female_mask & surv_mask])
female_dead_age = np.mean(age_np[female_mask & dead_mask])

# 35. Минимальная, максимальная и средняя стоимость билета
min_fare = np.min(fare_np)
max_fare = np.max(fare_np)
mean_fare = np.mean(fare_np)

# 36. Стандартное отклонение возраста
std_age = np.std(age_np)

numpy_table = pd.DataFrame({
    "Показатель": [
        "Общий процент выживших",
        "Процент выживших (мужчины)",
        "Процент выживших (женщины)",
        "Средний возраст (мужчины)",
        "Средний возраст (женщины)",
        "Средний возраст выживших мужчин",
        "Средний возраст погибших мужчин",
        "Средний возраст выживших женщин",
        "Средний возраст погибших женщин",
        "Минимальная стоимость билета",
        "Максимальная стоимость билета",
        "Средняя стоимость билета",
        "Стандартное отклонение возраста",
    ],
    "Значение": [
        f"{overall_surv:.2f}%",
        f"{male_surv:.2f}%",
        f"{female_surv:.2f}%",
        f"{male_age:.2f}",
        f"{female_age:.2f}",
        f"{male_surv_age:.2f}",
        f"{male_dead_age:.2f}",
        f"{female_surv_age:.2f}",
        f"{female_dead_age:.2f}",
        f"{min_fare:.2f}",
        f"{max_fare:.2f}",
        f"{mean_fare:.2f}",
        f"{std_age:.2f}",
    ]
})
print("\nРезультаты сравнительного анализа (NumPy):")
print(numpy_table.to_string(index=False))



# ЧАСТЬ V. Фильтрация данных

# Задание 1. Мужчины старше 30 лет, путешествовавшие первым классом
f1 = df[(df["Sex"] == "male") & (df["Age"] > 30) & (df["Pclass"] == 1)]
print(f"\nЗадание 1 (Мужчины > 30 лет, 1 класс): количество = {len(f1)}")
print(f1.head(10))

# Задание 2. Пассажиры моложе 18 лет или женщины, которые при этом выжили
f2 = df[((df["Age"] < 18) | (df["Sex"] == "female")) & (df["Survived"] == 1)]
print(f"\nЗадание 2 (Выжившие: младше 18 лет или женщины): количество = {len(f2)}")

# Задание 3. Пассажиры 3-го класса, стоимость билета которых выше средней в этом классе
mean_fare_3 = df[df["Pclass"] == 3]["Fare"].mean()
f3 = df[(df["Pclass"] == 3) & (df["Fare"] > mean_fare_3)]
print(f"\nЗадание 3 (3 класс с Fare > средней [{mean_fare_3:.2f}]): количество = {len(f3)}")

# Задание 4. Пассажиры от 20 до 40 лет включительно, отправившиеся из порта S
f4 = df[(df["Age"] >= 20) & (df["Age"] <= 40) & (df["Embarked"] == "S")]
print(f"\nЗадание 4 (Возраст 20–40 лет, порт S): количество = {len(f4)}")

# ЧАСТЬ VI. Группировка и агрегирование

# 37. Группировка по классу (Pclass) и полу (Sex)
stats_class_sex = (
    df.groupby(["Pclass", "Sex"])
    .agg(
        Количество_пассажиров=("PassengerId", "count"),
        Средний_возраст=("Age", "mean"),
        Доля_выживших_процент=("Survived", lambda x: np.mean(x == 1) * 100),
        Средняя_стоимость_билета=("Fare", "mean"),
    )
    .reset_index()
)
print("\n37. Группировка по Pclass и Sex:")
print(stats_class_sex.round(2))

# 38. Группировка по порту посадки (Embarked)
stats_embarked = (
    df.groupby("Embarked")
    .agg(
        Количество_пассажиров=("PassengerId", "count"),
        Процент_выживших=("Survived", lambda x: np.mean(x == 1) * 100),
    )
    .reset_index()
)
print("\n38. Группировка по Embarked:")
print(stats_embarked.round(2))

# 39. Класс пассажиров с наибольшей долей выживших
best_class = df.groupby("Pclass")["Survived"].mean().idxmax()
best_class_pct = df.groupby("Pclass")["Survived"].mean().max() * 100
print(f"\n39. Класс с наибольшей долей выживших: {best_class} класс ({best_class_pct:.2f}%)")



# ЧАСТЬ VII. Сохранение результатов

# 40. Сохранение обработанного DataFrame в titanic_processed.csv
df.to_csv("titanic_processed.csv", index=False)

# 41. Сохранение результатов группировки по классу и полу в titanic_statistics.csv
stats_class_sex.round(2).to_csv("titanic_statistics.csv", index=False)

# 42. Повторная загрузка для проверки корректности сохранения
check_processed = pd.read_csv("titanic_processed.csv")
check_stats = pd.read_csv("titanic_statistics.csv")
print(f"\n42. Проверка пройдена: titanic_processed.csv {check_processed.shape}, titanic_statistics.csv {check_stats.shape}")
