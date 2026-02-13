"""
Задача 1 (Вариант 18)
Программа для работы со списком, введенным пользователем.
Демонстрирует свою any, встроенную all и сортировку СЛИЯНИЕМ.
"""

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

def main_task1():
    """Основная функция для задачи 1."""
    print("-" * 30)
    print("Задача 1 (Сортировка СЛИЯНИЕМ)")
    print("-" * 30)

    # Ввод данных от пользователя
    input_str = input("Введите элементы списка через пробел: ")
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
        sorted_list = merge_sort(data_list)
        print(f"3. Отсортированный список (СЛИЯНИЕМ): {sorted_list}")
        print(f"   Исходный список не изменился: {data_list}")
    else:
        print("3. Невозможно отсортировать, так как список содержит не только числа.")

if __name__ == "__main__":
    main_task1()