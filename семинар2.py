#семинар ввс 2
# 1 уровень - описание тесты реализация + Cтрока пользователя
# 1 уровень - upper(), lover(),()capitalier() - методы
# 2 уровень - find(),replace(),count(),с помощью index()
# 3 уровень - split(),join()
# 4 уровень - isdigit(),isalpha()*format,strip()
# 5 "......pY+Hon;is;AWESoome....." +ALica
"""
text1='пРиВет_МИР'
text2='Ботать_это_круто'
text3='1,2,3,4'
text_4a="1234&%1$"
text_4b="____abc1234_____""

print(f"Меня зовут {age}
        /мне {age} лет")
f''
"""
"""

#1 уровень( выбор)
"a=str(input('Выбери метод: ')
def 1():
    print(f"Выбран метод {a} - все маленькие буквы
          / {text1.upper()})
    

def 2():
    print(f"Выбран метод {a} - все большие буквы
          / {text1.lover()})
def 3():
    print(f"Выбран метод {a} - С заглавной буквы
          / {text1.capitalize()})


if a == "upper":
    1()
elif a == "lover":
    2()
elif a == "capitalize":
    3()
else:
    print("Такого варианта нет")



"""
"""
# 2 уровень

a=int(input('Выбери метод: ')
def find():
    print(f"Выбран метод {a} - поиск строки)
          t=str(input("Введи то,что нужно найти ")
    print({text1.find(t)})
    

def replace():
    print(f"Выбран метод {a} - замена слова 
          / {})
    print("Введи слово, которое хочешь замменить, и слово, на какое заменить через пробед")
    t,s=map(str, input().split())
    print(text1.replace(t,s))
    
def count():
    print(f"Выбран метод {a} - посчитать количество букв)
          / {text1.count()})


if a == "find":
    find()
elif a == "replace":
    replace()
elif a == "count()":
    count()
else:
    print("Такого варианта нет")
# ТЕСТЫ 1. Позиция первого вхождения "круто" 2.заменить круто на любой символ 3. посчитать буквы "о")
"""
"""
# 3 уровевнь

a=int(input('Выбери метод: ')
def split():
    print(f"Выбран метод {a} - поиск строки)
          t=str(input("Введи то,что нужно найти ")
    print({text1.find(t)})
    

def join():
    print(f"Выбран метод {a} - замена слова 
          / {})
    print("Введи слово, которое хочешь замменить, и слово, на какое заменить через пробед")
    t,s=map(str, input().split())
    print(text1.replace(t,s))
    
def split_join():
    print(f"Выбран метод {a} - посчитать количество букв)
          / {text1.count()})


if a == "split":
    find()
elif a == "replace":
    replace()
elif a == "count()":
    count()
else:
    print("Такого варианта нет")
"""

# ==========================================
# БЛОК 1. Исходные переменные для тестов
# ==========================================
text1 = 'пРиВет_МИР'
text2 = 'Ботать_это_круто'
text3 = '1,2,3,4'
text_4a = "1234&%1$"
text_4b = "____abc1234_____"
text5 = "......pY+Hon;is;AWESoome....."

# Пользователь выбирает, какой уровень семинара запустить
lvl = input("Выбери уровень (1-5): ")


# ==========================================
# 1 УРОВЕНЬ: Работа с регистром (upper, lower, capitalize)
# ==========================================
if lvl == "1":
    print(f"Тестовая строка: {text1}")
    a = input('Выбери метод (upper / lower / capitalize): ')

    # Функции для вывода результатов работы методов
    def opt_upper(txt):
        print(f"Результат: {txt.upper()}")  # .upper() делает ВСЕ буквы заглавными

    def opt_lower(txt):
        print(f"Результат: {txt.lower()}")  # .lower() делает ВСЕ буквы строчными

    def opt_capitalize(txt):
        print(f"Результат: {txt.capitalize()}")  # .capitalize() делает заглавной только первую букву

    # 1. Запуск на готовом примере из задания
    print("\n--- Тестовый запуск ---")
    if a == "upper":
        opt_upper(text1)
    elif a == "lower":
        opt_lower(text1)
    elif a == "capitalize":
        opt_capitalize(text1)
    else:
        print("Такого варианта нет")

    # 2. Применение выбранного метода к тексту пользователя
    print("\n--- Твой ввод ---")
    user_txt = input("Введи свою строку: ")
    if a == "upper":
        opt_upper(user_txt)
    elif a == "lower":
        opt_lower(user_txt)
    elif a == "capitalize":
        opt_capitalize(user_txt)


# ==========================================
# 2 УРОВЕНЬ: Поиск, замена и подсчет (find, replace, count)
# ==========================================
elif lvl == "2":
    print(f"Тестовая строка: {text2}")
    a = input('Выбери метод (find / replace / count): ')

    # 1. Запуск демонстрационных тестов
    print("\n--- Тестовый запуск ---")
    if a == "find":
        # .find() возвращает индекс (номер) первого символа найденного слова
        print(f"Позиция слова 'круто': {text2.find('круто')}")
    elif a == "replace":
        # .replace('что', 'на что') заменяет одну подстроку на другую
        print(f"Замена 'круто' на '★': {text2.replace('круто', '★')}")
    elif a == "count":
        # .count() считает количество конкретных букв или слов
        print(f"Количество букв 'о': {text2.count('о')}")
    else:
        print("Такого варианта нет")

    # 2. Выполнение тех же операций для строки пользователя
    print("\n--- Твой ввод ---")
    user_txt = input("Введи свою строку: ")
    if a == "find":
        t = input("Что найти: ")
        print(f"Индекс: {user_txt.find(t)}")
    elif a == "replace":
        t = input("Что заменить: ")
        s = input("На что заменить: ")
        print(f"Результат: {user_txt.replace(t, s)}")
    elif a == "count":
        t = input("Какую букву/слово посчитать: ")
        print(f"Количество: {user_txt.count(t)}")


# ==========================================
# 3 УРОВЕНЬ: Разделение и склейка (split, join)
# ==========================================
elif lvl == "3":
    print(f"Тестовая строка: {text3}")
    a = input('Выбери метод (split / join / split_join): ')

    # 1. Демонстрационный запуск
    print("\n--- Тестовый запуск ---")
    if a == "split":
        # .split(',') разбивает строку на список элементов по разделителю (запятая)
        print(f"Разбиение по ',': {text3.split(',')}")
    elif a == "join":
        lst = ['1', '2', '3', '4']
        # ' - '.join(список) объединяет элементы списка в одну строку через тире
        print(f"Склейка тире: {' - '.join(lst)}")
    elif a == "split_join":
        # Замена разделителя: сначала разбиваем по ',', затем склеиваем через ' -> '
        print(f"Замена разделителя: {' -> '.join(text3.split(','))}")
    else:
        print("Такого варианта нет")

    # 2. Пользовательский ввод
    print("\n--- Твой ввод ---")
    if a == "split":
        user_txt = input("Введи строку: ")
        sep = input("Разделитель: ")
        print(user_txt.split(sep))
    elif a == "join":
        # .split() без аргументов режет введенную строку по пробелам на список
        words = input("Введи элементы через пробел: ").split()
        sep = input("Чем склеить: ")
        print(sep.join(words))
    elif a == "split_join":
        user_txt = input("Введи строку: ")
        old_sep = input("Старый разделитель: ")
        new_sep = input("Новый разделитель: ")
        print(new_sep.join(user_txt.split(old_sep)))


# ==========================================
# 4 УРОВЕНЬ: Проверки типов и очистка (isdigit, isalpha, format, strip)
# ==========================================
elif lvl == "4":
    print(f"Тестовые строки: A = '{text_4a}', B = '{text_4b}'")
    a = input('Выбери метод (isdigit / isalpha / format / strip): ')

    # 1. Демонстрационный запуск
    print("\n--- Тестовый запуск ---")
    if a == "isdigit":
        # .isdigit() проверяет, состоит ли строка ТОЛЬКО из цифр (True/False)
        print(f"Только цифры в A? {text_4a.isdigit()}")
    elif a == "isalpha":
        # .isalpha() проверяет, состоит ли строка ТОЛЬКО из букв (True/False)
        print(f"Только буквы в A? {text_4a.isalpha()}")
    elif a == "format":
        age = 18
        # f-строка (f"...") подставляет значение переменной age внутрь текста
        print(f"Меня зовут Алиса / мне {age} лет")
    elif a == "strip":
        # .strip('_') удаляет все знаки '_' только с концов (по краям) строки
        print(f"Убираем '_': {text_4b.strip('_')}")
    else:
        print("Такого варианта нет")

    # 2. Пользовательский ввод
    print("\n--- Твой ввод ---")
    if a == "format":
        name = input("Введи имя: ")
        age = input("Введи возраст: ")
        print(f"Меня зовут {name} / мне {age} лет")
    else:
        user_txt = input("Введи свою строку: ")
        if a == "isdigit":
            print(f"Только цифры? {user_txt.isdigit()}")
        elif a == "isalpha":
            print(f"Только буквы? {user_txt.isalpha()}")
        elif a == "strip":
            s = input("Символ для удаления с краев: ")
            print(f"Результат: {user_txt.strip(s)}")


# ==========================================
# 5 УРОВЕНЬ: Комплексная обработка "грязной" строки
# ==========================================
elif lvl == "5":
    print(f"Грязный тест: {text5}")
    
    # 1. Пошаговая цепочка методов (method chaining)
    print("\n--- Тестовый запуск ---")
    # .strip(".")      -> убирает точки по краям ("pY+Hon;is;AWESoome")
    # .replace("+","t")-> меняет '+' на 't' ("pYtHon;is;AWESoome")
    # .replace(";", " ")-> меняет ';' на пробелы ("pYtHon is AWESoome")
    # .capitalize()   -> приводить к нормальному виду ("Python is awesoome")
    clean_test = text5.strip(".").replace("+", "t").replace(";", " ").capitalize()
    print(f"Результат очистки + Алиса: {clean_test}")

    # 2. Комплексная очистка пользовательского ввода
    print("\n--- Твой ввод ---")
    user_txt = input("Введи грязную строку: ")
    strip_sym = input("Что убрать с краев: ")
    old_s = input("Какой символ заменить: ")
    new_s = input("На что заменить: ")
    
    # Все три метода применяются последовательно слева направо
    res = user_txt.strip(strip_sym).replace(old_s, new_s).capitalize()
    print(f"Итог: {res}")

else:
    print("Неверный уровень!")