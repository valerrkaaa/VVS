import math
from random import randint, uniform
from pprint import pprint

k = 4


def array_print(array):
    """
    Вывод в консоль значений одномерного массива
    """
    print(', '.join([str(i) for i in array]))


def d(x: float):
    """
    Отсекает целую часть
    Пример: 1,456 -> 0.456
    """
    return x - int(x)


def fill_array(n):
    """
    Создаёт одномерный массив случайных чисел в диапазоне от 0 до 1
    """
    out = [d(uniform(0, 1))]
    for i in range(n - 1):
        out.append(d(out[-1] * 9.5))
    return out


def get_i_from_float(a, i: int):
    """
    Возвращает i-тый элемент после запятой
    Пример: a=0,4567, i=3 -> 6
    """
    return int(a * (10 ** i) % 10)


def check_hi_borders(hi: float, hi_lower=3.32, hi_upper=16.9):
    """
    Проверка границ доверительного интервала
    """
    if hi > hi_lower:
        if hi < hi_upper:
            return True, 'Входит в доверительный интревал'
        return False, 'Больше верхней границы'
    return False, 'Меньше нижней границы'


def test_freq_and_pairs(arr):
    if len(arr) % 2 == 0:

        # создание массива со значениями от десятков до 2 * k
        # пример: 0.123... -> [1, 2, 3, .., 2 * k]
        e_arr = []
        for a in arr:
            e_arr.extend([get_i_from_float(a, i) for i in range(1, 2 * k + 1)])
        print('\nОдномерный массив:')
        array_print(e_arr)

        # разбиение на пары
        # пример: [1, 2, 3, 4] -> [(1, 2), (3, 4)]
        pairs_arr = [(e_arr[i], e_arr[i + 1]) for i in range(0, len(e_arr) - 1, 2)]
        print('\nМассив пар:')
        array_print(pairs_arr)

        # Создание матрицы 10 на 10 с подсчётом числа повторений
        # Пример: [(1, 1), (1, 0), (1, 1)] -> [[0, 0],
        #                                     [[1, 2]]
        matrix_array = [[0 for _ in range(10)] for _ in range(10)]
        for e in pairs_arr:
            matrix_array[e[0]][e[1]] += 1
        print('\nСформированная матрица:')
        pprint(matrix_array)

        # Считаем сумму элементов (vi - сумма i-того столбца, vj - сумма j-той строки)
        # Пример: [[0, 0],
        #         [[1, 2]] -> [1, 5]
        vi = []
        for i in range(len(matrix_array)):
            vi_sum = 0
            for j in range(len(matrix_array[i])):
                vi_sum += matrix_array[j][i] + matrix_array[i][j]
            vi.append(vi_sum)
        print('\nvi:')
        array_print(vi)

        # Считаем величину Хи-квадрат по формуле 1.13
        p = 0.1
        pN = p * len(e_arr)
        sum_i = 0
        for v in vi:
            sum_i += (v - pN) ** 2
        hi = 1 / pN * sum_i
        print(f'\nХи-квадрат(1.13) = {hi}')
        _, text = check_hi_borders(hi)
        print(text)

        # Считаем Хи-квадрат по формуле 1.14
        p = 0.01
        pN = p * len(e_arr)
        sum_i = 0
        for i in range(10):
            sum_j = 0
            for j in range(10):
                sum_j += (matrix_array[i][j] - pN) ** 2
            sum_i += sum_j
        hi = math.sqrt(1 / pN * sum_i)
        print(f'\nХи-квадрат(1.14) = {hi}')
        _, text = check_hi_borders(hi)
        print(text)
    else:
        print('Число элементов должно быть чётным!')


def main():
    # генерируем массив из 100 чисел:
    arr = fill_array(100)
    print('\nМассив чисел:')
    array_print(arr)

    # тест проверки частот и пар:
    test_freq_and_pairs(arr=arr)


if __name__ == '__main__':
    main()
