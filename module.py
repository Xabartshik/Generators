__author__ = 'Oshlakov'
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z139

# i
def G1(max_iter):
    """Генератор для задания 139 -- вычисление чисел от 1 до i"""
    x = 1
    for _ in range(max_iter):
        yield x
        x += 1
# i**2
def G2(max_iter):
    x = 1
    """Генератор для задания 139 -- вычисление квадратов чисел от 1 до i"""
    for _ in range(max_iter):
        yield x ** 2
        x += 1
# i!
def G3(max_iter):
    """Генератор для задания 139 -- вычисление факториалов от 1 до i"""
    x = 1
    for _ in range(max_iter):
        yield x
        x *= x + 1
#2**(i+1)
def G4(max_iter):
    """Генератор для задания 139 -- вычисление степеней 2 от (2) до (i + 1)"""
    x = 1
    for _ in range(max_iter):
        yield 2 ** (x + 1)
        x += 1
# 2**i + 3 ** (i + 1)
def G5(max_iter):
    """Генератор для задания 139 -- вычисление чисел по формуле 2**i + 3 ** (i + 1)"""
    x = 1
    for _ in range(max_iter):
        yield 2**x + 3 ** (x + 1)
        x += 1
# 2**i / i!
def G6(max_iter):
    """Генератор для задания 139 -- вычисление чисел по формуле 2**i / i!"""
    x = 1
    x_f = 1
    for _ in range(max_iter):
        yield 2**x / x_f
        x += 1
        x_f *= x
#Sum(1..i)(1/i)
def G7(max_iter):
    """Генератор для задания 139 -- вычисление суммы ряда чисел от (1..i) (1/i)"""
    x = 1
    l_val = 0
    for _ in range(max_iter):
        l_val += 1 / x
        yield l_val
        x += 1
#Sum(1..i)(1*(-1)**(i+1)/i)
def G8(max_iter):
    """Генератор для задания 139 -- вычисление суммы ряда чисел от (1..i) (1*(-1)**(i+1)/i)"""
    x = 1
    l_sign = 1
    l_val = 0
    for _ in range(max_iter):
        l_val += 1 / x * l_sign
        yield l_val
        l_sign *= -1
        x += 1
#Sum(1..i)(i(1/i!))
def G9(max_iter):
    """Генератор для задания 139 -- вычисление суммы ряда чисел от (1..i) (i(1/i!))"""
    x = 1
    l_val = 0
    l_fac = 1
    for _ in range(max_iter):
        l_val += 1 / l_fac
        yield x * l_val
        x += 1
        l_fac *= x
# Метод для проверки генераторов
def test_generators():
    """Проверка всех генераторов для задания 139"""

    # Тест для G1
    expected_G1 = [1, 2, 3, 4, 5]
    assert list(G1(5)) == expected_G1, "Тест для G1 не пройден"

    # Тест для G2
    expected_G2 = [1, 4, 9, 16, 25]
    assert list(G2(5)) == expected_G2, "Тест для G2 не пройден"

    # Тест для G3
    expected_G3 = [1, 2, 6, 42, 1806]
    assert list(G3(5)) == expected_G3, "Тест для G3 не пройден"

    # Тест для G4
    expected_G4 = [4, 8, 16, 32, 64]
    assert list(G4(5)) == expected_G4, "Тест для G4 не пройден"

    # Тест для G5
    expected_G5 = [11, 31, 89, 259, 761]
    assert list(G5(5)) == expected_G5, "Тест для G5 не пройден"

    # Тест для G6
    expected_G6 = [2.0, 2.0, 1.3333333333333333, 0.6666666666666666, 0.26666666666666666]
    result_G6 = list(G6(5))
    for i in range(len(result_G6)):
        assert abs(result_G6[i] - expected_G6[i]) < 1e-10, "Тест для G6 не пройден"

    # Тест для G7
    expected_G7 = [1.0, 1.5, 1.8333333333333333, 2.083333333333333, 2.283333333333333]
    result_G7 = list(G7(5))
    for i in range(len(result_G7)):
        assert abs(result_G7[i] - expected_G7[i]) < 1e-10, "Тест для G7 не пройден"

    # Тест для G8
    expected_G8 = [1.0, 0.5, 0.8333333333333333, 0.5833333333333333, 0.7833333333333332]
    result_G8 = list(G8(5))
    for i in range(len(result_G8)):
        assert abs(result_G8[i] - expected_G8[i]) < 1e-10, "Тест для G8 не пройден"

    # Тест для G9
    expected_G9 = [1.0, 3, 5.0, 6.833333333333334, 8.583333333333334]
    result_G9 = list(G9(5))
    for i in range(len(result_G9)):
        assert abs(result_G9[i] - expected_G9[i]) < 1e-10, "Тест для G9 не пройден"
