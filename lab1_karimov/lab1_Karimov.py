from random import randint, uniform


def show_array(array):
    print(' '.join([str(i) for i in array]))


def d(x):
    return x - int(x)


def fill_array(n):
    out = [d(uniform(0, 1))]
    for i in range(n - 1):
        out.append(d(out[-1] * 9.5))
    return out


def main():
    arr = fill_array(5)
    show_array(arr)


if __name__ == '__main__':
    main()
