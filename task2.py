"""
Задача 2 (№6 по варианту - CyclicTupleIterator)
Класс-итератор для бесконечного циклического обхода кортежа.
"""

import time
import random

class CyclicTupleIterator:
    """
    Циклический итератор для кортежа.
    При достижении последнего элемента начинает сначала.
    """
    
    def __init__(self, data):
        """Инициализация итератора."""
        if not isinstance(data, tuple):
            raise TypeError(f"Ожидается кортеж, получен {type(data).__name__}")
        
        self.data = data
        self.index = 0
        self.length = len(data)
        self.iterations = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Возвращает следующий элемент (циклически)."""
        if self.length == 0:
            raise StopIteration("Кортеж пуст")
        
        element = self.data[self.index]
        self.index = (self.index + 1) % self.length  # Циклический переход
        self.iterations += 1
        return element


def generate_random_tuple(size):
    """Генерирует кортеж случайных чисел."""
    return tuple(random.randint(1, 100) for _ in range(size))


def performance_test():
    """Тест производительности с разными размерами кортежей."""
    print("=" * 60)
    print("ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ ЗАДАЧИ 2")
    print("=" * 60)
    
    # Тестируем разные размеры кортежей
    test_sizes = [10, 100, 1000, 10000, 100000]
    iterations = 1_000_000  # 1 млн итераций для каждого теста
    
    print(f"\nТест с {iterations:,} итераций для каждого размера:\n")
    print(f"{'Размер':>10} | {'Время (сек)':>12} | {'итер/сек':>12} | {'Память (КБ)':>12}")
    print("-" * 60)
    
    for size in test_sizes:
        # Генерируем кортеж
        test_tuple = generate_random_tuple(size)
        
        # Создаем итератор
        iterator = CyclicTupleIterator(test_tuple)
        
        # Замер времени
        start = time.time()
        for _ in range(iterations):
            next(iterator)
        end = time.time()
        
        total_time = end - start
        speed = iterations / total_time
        
        # Память (приблизительно)
        memory_kb = (test_tuple.__sizeof__() + iterator.__sizeof__()) / 1024
        
        print(f"{size:10,d} | {total_time:12.3f} | {speed:12,.0f} | {memory_kb:12.2f}")
    
    print("=" * 60)


def main_task2():
    """Основная функция."""
    print("Задача 2: CyclicTupleIterator")
    print("-" * 40)
    
    # Простая демонстрация
    test_tuple = (10, 20, 30, 40, 50)
    print(f"Кортеж: {test_tuple}")
    
    iterator = CyclicTupleIterator(test_tuple)
    print("Первые 12 элементов (циклически):")
    for i in range(12):
        print(f"  {i+1}: {next(iterator)}")
    
    print("\n" + "-" * 40)
    print("Запуск теста производительности...\n")
    performance_test()


if __name__ == "__main__":
    main_task2()