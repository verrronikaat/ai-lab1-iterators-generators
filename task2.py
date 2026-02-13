"""
Задача 2 (№6 по варианту - CyclicTupleIterator)
Класс-итератор для бесконечного циклического обхода кортежа.
При достижении последнего элемента начинает итерацию сначала.
"""

class CyclicTupleIterator:
    """
    Циклический итератор для кортежа.
    Итерируется по элементам кортежа бесконечно.
    """
    
    def __init__(self, data):
        """
        :param data: исходный кортеж для итерации
        """
        if not isinstance(data, tuple):
            raise TypeError("Ожидается кортеж (tuple)")
        
        self.data = data
        self.index = 0
        
        # Проверка на пустой кортеж
        if len(data) == 0:
            print("Предупреждение: кортеж пуст, итератор не будет выдавать элементы")
    
    def __iter__(self):
        """Возвращает сам итератор."""
        return self
    
    def __next__(self):
        """
        Возвращает следующий элемент из кортежа.
        Если индекс вышел за границы, сбрасываем его в 0 и продолжаем.
        """
        # Если кортеж пуст, нет элементов для выдачи
        if len(self.data) == 0:
            raise StopIteration("Кортеж пуст, итерация невозможна")
        
        # Получаем текущий элемент
        current_element = self.data[self.index]
        
        # Сдвигаем индекс для следующего вызова
        self.index += 1
        
        # Если дошли до конца, начинаем сначала
        if self.index >= len(self.data):
            self.index = 0
            print("  (достигнут конец, начинаем сначала)")
        
        return current_element


class CyclicTupleIteratorV2:
    """
    Альтернативная реализация с использованием цикла while и yield.
    Это генераторная функция, которая тоже создает итератор.
    """
    
    def __init__(self, data):
        if not isinstance(data, tuple):
            raise TypeError("Ожидается кортеж (tuple)")
        self.data = data
    
    def __iter__(self):
        """Генераторная функция для бесконечного циклического обхода."""
        if len(self.data) == 0:
            return  # Пустой генератор
        
        while True:  # Бесконечный цикл
            for element in self.data:
                yield element


def main_task2():
    """Демонстрация работы CyclicTupleIterator."""
    print("-" * 40)
    print("Задача 2 (CyclicTupleIterator)")
    print("-" * 40)
    
    # Тест 1: Обычный кортеж с числами
    print("Тест 1: Кортеж с числами")
    tuple1 = (1, 2, 3, 4, 5)
    print(f"Исходный кортеж: {tuple1}")
    
    # Создаем циклический итератор
    cyclic_iter = CyclicTupleIterator(tuple1)
    
    print("Делаем 12 шагов итерации (больше, чем элементов в кортеже):")
    for i in range(12):
        try:
            element = next(cyclic_iter)
            print(f"  Шаг {i+1:2d}: {element}")
        except StopIteration as e:
            print(f"  Ошибка: {e}")
            break
    
    print()  # Пустая строка
    
    # Тест 2: Кортеж со строками
    print("Тест 2: Кортеж со строками")
    tuple2 = ("яблоко", "банан", "апельсин")
    print(f"Исходный кортеж: {tuple2}")
    
    cyclic_iter2 = CyclicTupleIterator(tuple2)
    
    print("Делаем 7 шагов итерации:")
    for i in range(7):
        element = next(cyclic_iter2)
        print(f"  Шаг {i+1}: {element}")
    
    print()  # Пустая строка
    
    # Тест 3: Смешанный кортеж
    print("Тест 3: Смешанный кортеж")
    tuple3 = (42, "hello", 3.14, True, None)
    print(f"Исходный кортеж: {tuple3}")
    
    cyclic_iter3 = CyclicTupleIterator(tuple3)
    
    print("Первые 10 элементов (бесконечный цикл):")
    for i, element in enumerate(cyclic_iter3):
        print(f"  {i+1}: {element}")
        if i >= 9:  # Останавливаемся после 10 элементов
            print("  ... (остановка для демонстрации)")
            break
    
    print()  # Пустая строка
    
    # Тест 4: Пустой кортеж
    print("Тест 4: Пустой кортеж")
    tuple4 = ()
    print(f"Исходный кортеж: {tuple4}")
    
    try:
        cyclic_iter4 = CyclicTupleIterator(tuple4)
        element = next(cyclic_iter4)
        print(f"  Получили: {element}")
    except StopIteration as e:
        print(f"  Ожидаемая ошибка: {e}")
    except TypeError as e:
        print(f"  Ошибка типа: {e}")
    
    print()  # Пустая строка
    print("-" * 40)
    
    # Демонстрация альтернативной реализации
    print("Альтернативная реализация (CyclicTupleIteratorV2 с yield):")
    tuple5 = (10, 20, 30)
    print(f"Кортеж: {tuple5}")
    
    cyclic_iter_v2 = CyclicTupleIteratorV2(tuple5)
    
    print("Первые 8 элементов:")
    count = 0
    for element in cyclic_iter_v2:
        print(f"  {element}")
        count += 1
        if count >= 8:
            print("  ... (остановка)")
            break


def demonstrate_in_for_loop():
    """Демонстрация использования в цикле for с ограничением."""
    print("\n" + "=" * 40)
    print("Демонстрация в цикле for с break")
    print("=" * 40)
    
    colors = ("красный", "зеленый", "синий")
    print(f"Цвета: {colors}")
    
    # Создаем итератор
    color_iter = CyclicTupleIterator(colors)
    
    # Используем в цикле for, но с принудительным выходом
    print("Циклический вывод цветов (10 итераций):")
    for i, color in enumerate(color_iter):
        print(f"  Итерация {i+1}: {color}")
        if i >= 9:  # Останавливаемся после 10 элементов
            break


if __name__ == "__main__":
    main_task2()
    demonstrate_in_for_loop()