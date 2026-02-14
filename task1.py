"""
Задача 1 (Вариант 18)
Программа для работы со списком, введенным пользователем.
Демонстрирует свою any, встроенную all и сортировку СЛИЯНИЕМ.
"""

import time
import random
import sys

def custom_any(iterable):
    """
    Своя реализация функции any().
    Возвращает True, если хоть один элемент итерируемого объекта истинен (положительное число).
    """
    for element in iterable:
        # Проверяем, является ли элемент положительным числом
        if isinstance(element, (int, float)) and element > 0:
            return True
    return False

def merge_sort(arr):
    """
    Сортировка СЛИЯНИЕМ (Merge Sort).
    Рекурсивно делит список на части, сортирует и объединяет их.
    Возвращает НОВЫЙ отсортированный список (не изменяет исходный).
    """
    # Базовый случай: список из 0 или 1 элемента уже отсортирован
    if len(arr) <= 1:
        return arr.copy()  # Возвращаем копию, чтобы не изменять оригинал
    
    # Разделяем список на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Рекурсивно сортируем обе половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Объединяем отсортированные половины
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Вспомогательная функция для слияния двух отсортированных списков.
    """
    result = []
    i = j = 0
    
    # Сравниваем элементы из левого и правого списков
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавляем оставшиеся элементы из левого списка
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Добавляем оставшиеся элементы из правого списка
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def performance_test():
    """
    Тест производительности сортировки слиянием на 1 миллионе элементов.
    """
    print("\n" + "=" * 60)
    print("ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ ЗАДАЧИ 1")
    print("=" * 60)
    
    # Генерируем 1 миллион случайных чисел
    print("Генерация 1,000,000 случайных чисел...")
    start_gen = time.time()
    
    # Генерируем список из 1 млн случайных чисел от 0 до 10,000
    test_data = [random.randint(0, 10000) for _ in range(1_000_000)]
    
    end_gen = time.time()
    gen_time = end_gen - start_gen
    print(f"Время генерации: {gen_time:.2f} секунд")
    print(f"Размер списка: {len(test_data):,} элементов")
    
    # Показываем первые 10 элементов для примера
    print(f"Первые 10 элементов: {test_data[:10]}")
    
    # Измеряем память (примерно)
    size_in_mb = sys.getsizeof(test_data) / (1024 * 1024)
    print(f"Приблизительный размер в памяти: {size_in_mb:.2f} МБ")
    
    # Тест сортировки
    print("\nЗапуск сортировки слиянием...")
    start_sort = time.time()
    
    sorted_data = merge_sort(test_data)
    
    end_sort = time.time()
    sort_time = end_sort - start_sort
    
    print(f"Время сортировки: {sort_time:.2f} секунд")
    print(f"Общее время: {gen_time + sort_time:.2f} секунд")
    
    # Проверка, что список действительно отсортирован
    is_sorted = all(sorted_data[i] <= sorted_data[i+1] for i in range(min(10, len(sorted_data)-1)))
    print(f"Первые 10 элементов после сортировки: {sorted_data[:10]}")
    print(f"Последние 10 элементов: {sorted_data[-10:]}")
    print(f"Сортировка выполнена успешно: {is_sorted and len(sorted_data) == 1_000_000}")
    
    # Вывод производительности
    print("\n" + "-" * 40)
    print("ИТОГИ ТЕСТИРОВАНИЯ:")
    print(f"Количество элементов: 1,000,000")
    print(f"Время сортировки: {sort_time:.2f} сек")
    print(f"Элементов в секунду: {1_000_000 / sort_time:.0f}")
    print(f"Сложность алгоритма: O(n log n)")
    print("-" * 40)
    
    # Сравнение со встроенной сортировкой Python (для справки)
    print("\nСравнение со встроенной сортировкой (TimSort):")
    test_copy = test_data.copy()
    start_builtin = time.time()
    test_copy.sort()
    end_builtin = time.time()
    builtin_time = end_builtin - start_builtin
    print(f"Встроенная сортировка: {builtin_time:.2f} сек")
    print(f"Разница: {sort_time / builtin_time:.1f}x медленнее")
    
    return sort_time

def main_task1():
    """Основная функция для задачи 1."""
    print("-" * 30)
    print("Задача 1 (Сортировка СЛИЯНИЕМ)")
    print("-" * 30)

    # Ввод данных от пользователя
    input_str = input("Введите элементы списка через пробел (или 'test' для запуска теста производительности): ")
    
    # Проверка на тестовый режим
    if input_str.lower() == 'test':
        performance_test()
        return
    
    # Разбиваем строку на части
    items = input_str.split()

    # Пытаемся преобразовать элементы в числа (int или float)
    data_list = []
    for item in items:
        try:
            # Сначала пробуем преобразовать в int
            data_list.append(int(item))
        except ValueError:
            try:
                # Если не получилось, пробуем во float
                data_list.append(float(item))
            except ValueError:
                # Если и это не число, оставляем как строку
                data_list.append(item)

    print(f"Исходный список: {data_list}")

    # 1. Своя функция custom_any
    has_positive = custom_any(data_list)
    print(f"1. Есть ли положительное число? (custom_any): {has_positive}")

    # 2. Встроенная функция all для проверки, что все элементы - числа
    # Используем генераторное выражение для проверки типа каждого элемента
    all_are_numbers = all(isinstance(x, (int, float)) for x in data_list)
    print(f"2. Все элементы - числа? (built-in all): {all_are_numbers}")

    # 3. Сортировка СЛИЯНИЕМ (только если все элементы - числа)
    if all_are_numbers:
        # Сортируем с помощью merge_sort (возвращает новый список)
        start_time = time.time()
        sorted_list = merge_sort(data_list)
        end_time = time.time()
        
        print(f"3. Отсортированный список (СЛИЯНИЕМ): {sorted_list}")
        print(f"   Исходный список не изменился: {data_list}")
        print(f"   Время сортировки: {(end_time - start_time)*1000:.2f} мс")
    else:
        print("3. Невозможно отсортировать, так как список содержит не только числа.")

if __name__ == "__main__":
    main_task1()