"""
Задача 3 (№9 по варианту - Генератор паролей)
Функция-генератор для создания последовательности
случайных паролей заданной длины N=8.
"""

from string import ascii_lowercase, ascii_uppercase
from random import choice
import time

# Набор символов для генерации паролей
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N = 8  # Длина пароля согласно варианту

def password_generator(limit, n=N):
    """
    Функция-генератор для создания паролей с ограничением по количеству.
    
    Аргументы:
        limit (int): количество паролей для генерации
        n (int): длина каждого пароля (по умолчанию N=8)
    
    Возвращает:
        generator: генератор, выдающий строки-пароли
    """
    count = 0
    while count < limit:  # Условие вместо while True
        password = ''.join(choice(chars) for _ in range(n))
        yield password
        count += 1
    # Генератор автоматически завершается после генерации limit паролей


def main_task3():
    """Основная функция для демонстрации работы генератора паролей."""
    print("=" * 60)
    print("Задача 3: Генератор случайных паролей (N=8)")
    print("=" * 60)
    
    # Параметры теста
    num_passwords = 1_000_000  # 1 миллион паролей
    
    print(f"Генерация {num_passwords:,} паролей...")
    print(f"Длина пароля: {N} символов")
    print(f"Набор символов: {len(chars)} символов")
    print("-" * 60)
    
    # Замер времени
    start_time = time.time()
    
    # Создаем генератор
    gen = password_generator(num_passwords)
    
    # Генерируем пароли и сохраняем первые 5 для примера
    first_passwords = []
    count = 0
    
    for password in gen:
        count += 1
        if count <= 5:
            first_passwords.append(password)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Вывод результатов
    print(f"Сгенерировано: {count:,} паролей")
    print(f"Время выполнения: {total_time:.2f} секунд")
    print(f"Скорость: {count / total_time:,.0f} паролей/сек")
    print(f"Время на 1 пароль: {(total_time / count) * 1000:.3f} мс")
    print("-" * 60)
    print("Первые 5 сгенерированных паролей:")
    for i, pwd in enumerate(first_passwords, 1):
        print(f"  {i}. {pwd}")
    print("=" * 60)


if __name__ == "__main__":
    main_task3()