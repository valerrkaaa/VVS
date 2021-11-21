from random import randint, uniform
from pprint import pprint

k = 4


def array_print(array):
    """
    Вывод в консоль значений одномерного массива
    """
    print(' '.join([str(i) for i in array]))


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


def test_freq_and_pairs(arr):
    if len(arr) % 2 == 0:

        # создание массива со значениями от десятков до 2 * k
        # пример: 0.123... -> [1, 2, 3, .., 2 * k]
        e_arr = []
        for a in arr:
            e_arr.extend([get_i_from_float(a, i) for i in range(1, 2 * k)])

        # разбиение на пары
        # пример: [1, 2, 3, 4] -> [(1, 2), (3, 4)]
        pairs_arr = [(e_arr[i], e_arr[i + 1]) for i in range(0, len(e_arr) - 1, 2)]

        # Создание матрицы 10 на 10 с подсчётом числа повторений
        matrix_array = [[0 for _ in range(10)] for _ in range(10)]
        for e in pairs_arr:
            matrix_array[e[0]][e[1]] += 1
        pprint(matrix_array)

    else:
        return -1


def main():
    arr = fill_array(100)
    array_print(arr)
    test_freq_and_pairs(arr)


if __name__ == '__main__':
    main()
    # print(test_freq_and_pairs(0.123456, 6))
