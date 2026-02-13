"""
Задача 4 (№12 по варианту - BinomialSequence)
Класс-генератор для получения n-й строки треугольника Паскаля
(биномиальных коэффициентов) с минимальным использованием памяти.
"""

class BinomialSequence:
    """
    Генератор биномиальных коэффициентов (строки треугольника Паскаля).
    """
    @staticmethod
    def generate(n):
        """
        Генерирует последовательность C(n, 0), C(n, 1), ..., C(n, n).

        Аргументы:
            n (int): номер строки треугольника Паскаля (неотрицательное целое).

        Возвращает:
            generator: генератор, выдающий числа по одному.
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("n должно быть неотрицательным целым числом")

        # Первый коэффициент C(n, 0) всегда равен 1
        coefficient = 1
        yield coefficient

        # Вычисляем последующие коэффициенты на основе предыдущего
        # Используем формулу: C(n, k) = C(n, k-1) * (n - k + 1) / k
        for k in range(1, n + 1):
            # Пересчитываем коэффициент
            coefficient = coefficient * (n - k + 1) // k
            yield coefficient

def main_task4():
    """Демонстрация работы BinomialSequence."""
    print("-" * 30)
    print("Задача 4 (BinomialSequence)")
    print("-" * 30)

    test_n = 8  # N=8 из варианта
    print(f"Генерация {test_n}-й строки треугольника Паскаля:")

    # Создаем генератор
    gen = BinomialSequence.generate(test_n)

    print("Результат (выводим по одному числу):")
    # Итерируемся по генератору
    coefficients = []
    for i, coeff in enumerate(gen):
        print(f"  C({test_n},{i}) = {coeff}")
        coefficients.append(coeff)

    print(f"\nПолная строка: {coefficients}")

    # Проверка для других значений
    print("\n" + "-" * 20)
    for n in [0, 1, 2, 5]:
        print(f"Строка {n}: {list(BinomialSequence.generate(n))}")

if __name__ == "__main__":
    main_task4()