"""
Задача 3 (№9 по варианту - Генератор паролей)
Функция-генератор для создания бесконечной последовательности
случайных паролей заданной длины N=8.
"""

from string import ascii_lowercase, ascii_uppercase
from random import choice
from collections.abc import Iterator, Generator

# ИСПРАВЛЕНО: ascii_uppercase (было asimi_uppercase)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N = 8  # Длина пароля согласно варианту

def password_generator(n=N):
    """
    Функция-генератор для создания бесконечной последовательности паролей.
    
    Аргументы:
        n (int): длина каждого генерируемого пароля (по умолчанию N=8)
    
    Возвращает:
        generator: генератор, выдающий строки-пароли один за другим
    """
    while True:  # Бесконечный цикл для неограниченной генерации
        # Генерируем один пароль длиной n
        password = ''
        for _ in range(n):
            # Выбираем случайный символ из доступного набора
            password += choice(chars)
        
        # Возвращаем сгенерированный пароль
        yield password


def password_generator_comprehension(n=N):
    """
    Альтернативная реализация с использованием генераторного выражения
    и join для более компактного кода.
    """
    while True:
        # Используем генераторное выражение внутри join
        yield ''.join(choice(chars) for _ in range(n))


def password_generator_with_counter(n=N):
    """
    Расширенная версия генератора, которая также подсчитывает
    количество сгенерированных паролей.
    """
    count = 0
    while True:
        count += 1
        password = ''.join(choice(chars) for _ in range(n))
        yield count, password


def main_task3():
    """Основная функция для демонстрации работы генератора паролей."""
    print("=" * 60)
    print("Задача 3: Генератор случайных паролей")
    print("=" * 60)
    
    print(f"Набор символов для генерации: {chars}")
    print(f"Длина пароля: {N} символов")
    print(f"Общее количество возможных символов: {len(chars)}")
    print(f"Теоретическое количество вариантов: {len(chars)**N:,}")
    print("-" * 60)
    
    # Создаем генератор
    gen = password_generator()
    
    print("Первые 5 сгенерированных паролей:")
    print("-" * 40)
    
    # Выводим первые 5 паролей
    for i in range(5):
        password = next(gen)
        print(f"Пароль {i+1}: {password}")
    
    print("-" * 40)
    print("Генератор готов выдавать следующие пароли бесконечно...")
    
    # Демонстрация следующего пароля (6-й)
    next_password = next(gen)
    print(f"Следующий пароль (6-й): {next_password}")
    
    print("\n" + "=" * 60)
    print("Демонстрация альтернативной реализации:")
    print("=" * 60)
    
    # Используем альтернативную реализацию
    gen2 = password_generator_comprehension()
    
    print("Еще 3 пароля (альтернативная реализация):")
    for i in range(3):
        print(f"  {i+1}: {next(gen2)}")
    
    print("\n" + "=" * 60)
    print("Демонстрация генератора со счетчиком:")
    print("=" * 60)
    
    # Используем генератор со счетчиком
    gen3 = password_generator_with_counter()
    
    print("Первые 3 пароля с номерами:")
    for _ in range(3):
        count, pwd = next(gen3)
        print(f"  Пароль #{count}: {pwd}")


def demonstrate_generator_properties():
    """Демонстрация свойств генератора."""
    print("\n" + "=" * 60)
    print("Свойства генератора:")
    print("=" * 60)
    
    # Создаем генератор
    gen = password_generator()
    
    # Проверяем тип
    print(f"Тип объекта: {type(gen)}")
    
    # Проверяем, что это итератор
    print(f"Является ли итератором (Iterator): {isinstance(gen, Iterator)}")
    print(f"Является ли генератором (Generator): {isinstance(gen, Generator)}")
    
    # Демонстрация ленивых вычислений
    print("\nГенератор не хранит все пароли в памяти,")
    print("а вычисляет их по одному по запросу.")
    
    # Проверка возможности многократной итерации с ограничением
    print("\nДемонстрация одноразовости генератора:")
    gen_copy = password_generator()
    
    print("Первый проход (3 пароля):", end=" ")
    passwords_first = []
    for i, p in enumerate(gen_copy):
        passwords_first.append(p)
        print(p, end=" ")
        if i >= 2:  # Останавливаемся после 3 паролей
            break
    print()  # Новая строка
    
    print("Второй проход по тому же генератору (должен быть пустым):", end=" ")
    passwords_second = []
    for i, p in enumerate(gen_copy):
        passwords_second.append(p)
        print(p, end=" ")
        if i >= 2:  # Останавливаемся после 3 паролей, но генератор уже пуст
            break
    
    if not passwords_second:
        print("(ничего не выведено - генератор исчерпан)")
    else:
        print()  # Новая строка, если что-то вывелось
    
    print(f"\nПервый проход дал {len(passwords_first)} паролей")
    print(f"Второй проход дал {len(passwords_second)} паролей")


def generate_passwords_with_limit(limit=10):
    """
    Функция для генерации заданного количества паролей.
    Демонстрирует практическое использование генератора.
    """
    print(f"\nГенерация {limit} паролей для использования:")
    gen = password_generator()
    
    # Генерируем список из limit паролей
    passwords = [next(gen) for _ in range(limit)]
    
    # Выводим в удобном формате
    for i, pwd in enumerate(passwords, 1):
        print(f"{i:2d}. {pwd}")
    
    return passwords


def analyze_password_strength():
    """Анализ сложности генерируемых паролей."""
    gen = password_generator()
    sample_size = 100
    
    print("\nАнализ 100 сгенерированных паролей:")
    
    stats = {
        'has_lower': 0,
        'has_upper': 0,
        'has_digit': 0,
        'has_special': 0
    }
    
    for _ in range(sample_size):
        pwd = next(gen)
        if any(c.islower() for c in pwd):
            stats['has_lower'] += 1
        if any(c.isupper() for c in pwd):
            stats['has_upper'] += 1
        if any(c.isdigit() for c in pwd):
            stats['has_digit'] += 1
        if any(c in "!?@#$*" for c in pwd):
            stats['has_special'] += 1
    
    for key, value in stats.items():
        print(f"{key}: {value}/{sample_size} ({value/sample_size*100:.1f}%)")
    
    # Дополнительный анализ: средняя длина пароля (всегда N, но для демонстрации)
    print(f"\nДлина каждого пароля: {N} символов (фиксировано)")


if __name__ == "__main__":
    main_task3()
    demonstrate_generator_properties()
    generate_passwords_with_limit(8)
    
    print("\n" + "=" * 60)
    print("Практический пример: проверка паролей на уникальность")
    print("=" * 60)
    
    # Генерируем 20 паролей и проверяем на повторы
    gen = password_generator()
    passwords_set = set()
    duplicates = []
    
    for i in range(20):
        pwd = next(gen)
        if pwd in passwords_set:
            duplicates.append(pwd)
        else:
            passwords_set.add(pwd)
    
    print(f"Сгенерировано 20 паролей")
    print(f"Уникальных: {len(passwords_set)}")
    if duplicates:
        print(f"Найдены повторы: {duplicates}")
    else:
        print("Повторов не найдено (хорошее распределение)")
    
    # Добавляем анализ сложности
    analyze_password_strength()