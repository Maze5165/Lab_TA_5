# -*- coding: utf-8 -*-
import re
from collections import Counter

print("=== ЗАВДЮВАННЯ 2: Демонстрація методів ===")

print("\n--- Списки ---")
my_list = [3, 1, 4, 1, 5]
print(f"Початковий список: {my_list}")

my_list.append(9)
my_list.sort()
print(f"Після append(9) та sort(): {my_list}")

sliced = my_list[1:4]
print(f"Зріз [1:4]: {sliced}")

my_list.remove(1)
print(f"Після remove(1): {my_list}")

print("\n--- Кортежі ---")
my_tuple = (10, 20, 30)
print(f"Кортеж: {my_tuple}")
print(f"Елемент з індексом 1: {my_tuple[1]}")

try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"Спроба змінити кортеж викликала помилку: {e}")

print("\n--- Множини ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Множина A: {set_a}, Множина B: {set_b}")

union_set = set_a.union(set_b)
inter_set = set_a.intersection(set_b)

print(f"Об'єднання (A | B): {union_set}")
print(f"Перетин (A & B): {inter_set}")

print("\n--- Словники ---")
my_dict = {'name': 'Student', 'course': 1}
print(f"Словник: {my_dict}")

my_dict['grade'] = 95
keys = list(my_dict.keys())

print(f"Оновлений словник: {my_dict}")
print(f"Список ключів: {keys}")


print("\n" + "="*40 + "\n")


print("=== ЗАВДАННЯ 3: Аналіз тексту ===")
text = "Case-insensitive matching matters."
print(f"Вхідний текст: '{text}'\n")

words_list = re.findall(r"\w+", text.lower())
print(f"1. Список слів: {words_list}")

unique_words = set(words_list)
print(f"2. Множина унікальних слів: {unique_words}")

sorted_words = tuple(sorted(words_list, key=len))
print(f"3. Кортеж слів за довжиною: {sorted_words}")

word_counts = dict(Counter(words_list))
print(f"4. Словник частот: {word_counts}")

print(f"5. Статистика:")
print(f"   - Загальна кількість слів: {len(words_list)}")
print(f"   - Унікальних слів: {len(unique_words)}")
top_5 = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:5]
print(f"   - Топ слів за частотою: {top_5}")


print("\n" + "="*40 + "\n")


print("=== ЗАВДАННЯ 4: Обробка числового списку ===")
numbers = [6, 6, 6, 3, 9, 12]
print(f"Вхідний список: {numbers}\n")

seen = set()
no_dups_ordered = [x for x in numbers if not (x in seen or seen.add(x))]
print(f"1. Список без дублікатів: {no_dups_ordered}")

even_set = {x for x in numbers if x % 2 == 0}
print(f"2. Множина парних чисел: {even_set}")

sorted_nums = sorted(numbers)
min_5_tuple = tuple(sorted_nums[:5])
print(f"3. Кортеж 5 мінімальних чисел: {min_5_tuple}")

pos_dict = {i: val for i, val in enumerate(numbers)}
print(f"4. Словник (позиція: значення): {pos_dict}")

print(f"5. Статистика:")
print(f"   - Кількість елементів: {len(numbers)}")
print(f"   - Кількість дублікатів: {len(numbers) - len(set(numbers))}")
print(f"   - Мін: {min(numbers)}, Макс: {max(numbers)}")


print("\n" + "="*40 + "\n")


print("=== ЗАВДАННЯ 5 ===")
print("Умова: Є кортеж температур за тиждень. Створити множину унікальних значень і середню температуру.")

temps_tuple = (18, 20, 18, 22, 21, 20, 19)
print(f"Вхідний кортеж температур: {temps_tuple}")

unique_temps = set(temps_tuple)
print(f"Множина унікальних температур: {unique_temps}")

avg_temp = sum(temps_tuple) / len(temps_tuple)
print(f"Середня температура: {avg_temp:.2f}")