import math

message = 'Добро пожаловать в самую лучшую программу для вычисления \
квадратного корня из заданного числа'


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number: float) -> None:
    """Вычисляет итоговое значение."""
    if your_number <= 0:
        return
    result: float = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {result}')


print(message)
calc(25.5)
