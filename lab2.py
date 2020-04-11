import numpy as np
import matplotlib.pyplot as plt


def plot_method(xs, ys, h, title):
    plt.plot(xs, ys)
    plt.title(title)
    plt.plot(*get_original_function(a, b))
    plt.xlabel('Шаг= ' + str(h))
    plt.legend(['Приближение', 'Искомая функция'])
    plt.show()


def Eiler_method(f, a, b, N, y0):
    h = (b - a) / N
    xs = np.arange(a, b, h)
    ys = np.zeros(len(xs))
    n = 1
    ys[0] = y0
    for xn in xs[:-1]:
        yn = ys[n - 1]
        ys[n] = yn + h * f(xn, yn)
        n += 1
    plot_method(xs, ys, h, 'Метод Эйлера')


def Cauchy_method(f, a, b, N, y0):
    h = (b - a) / N
    xs = np.arange(a, b, h)
    xs2 = xs + h / 2
    ys = np.zeros(len(xs))
    n = 1
    ys[0] = y0
    for xn, xn2 in zip(xs[:-1], xs2[:-1]):
        yn = ys[n - 1]
        ys[n] = yn + h * f(xn2, yn + h * f(xn, yn) / 2)
        n += 1
    plot_method(xs, ys, h, 'Метод Коши')


def Taylor_method(f, df, ddf, a, b, N, y0):
    h = (b - a) / N
    xs = np.arange(a, b, h)
    ys = np.zeros(len(xs))
    n = 1
    ys[0] = y0
    for xn in xs[:-1]:
        yn = ys[n - 1]
        ys[n] = yn + h * f(xn, yn) + (h ** 2) / 2 * df(xn, yn) + (h ** 3) / 6 * ddf(xn, yn)
        n += 1
    plot_method(xs, ys, h, 'Метод Тейлора третьего порядка')


def get_original_function(a, b):
    h = 0.01
    x = np.arange(a, b, h)
    y = 0.1 * np.exp(50 * ((x ** 3) / 3 - (1.45 * x ** 2) / 2 + 0.51 * x))
    return x, y


if __name__ == '__main__':
    f = lambda x, y: 50 * y * (x - 0.6) * (x - 0.85)
    df = lambda x, y: 50 * y * ((2 * x - 1.45) + 50 * (x ** 2 - 1.45 * x + 0.51) ** 2)
    ddf = lambda x, y: 100 * (y + (2 * x - 1.45) * f(x, y)) + 50 * (x ** 2 - 1.45 * x + 0.51) * df(x, y)
    a = 0
    b = 1
    N = int(input('Введите число разбиений:'))
    y0 = 0.1
    Eiler_method(f, a, b, N, y0)
    Cauchy_method(f, a, b, N, y0)
    Taylor_method(f, df, ddf, a, b, N, y0)
