# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

fac = np.math.factorial


def yx(x, y):
    return x * y ** (1 / 3)


def yxx(x, y):
    return y**(1 / 3) + (1 / 3) * x**2 * y**(-(1 / 3))


def yxxx(x, y):
    return x * y**(-(1 / 3)) - (1 / 9) * x**3 * (1 / y)


def yxxxx(x, y):
    return y**(-(1 / 3)) - (2 / 3) * x**2 * (1 / y) + (1 / 9) * x**4 * y**(-(5 / 3))


def next_step(x, y, h):
    return y + yx(x, y) * h + (1 / 2) * yxx(x, y) * h**2 + (1 / fac(3)) * \
        yxxx(x, y) * h**3 + (1 / fac(4)) * yxxxx(x, y) * h**4


def exact(x):
    return ((x ** 2 + 2) / 3)**(3 / 2)


if __name__ == "__main__":
    h = 2
    y0 = 1
    x0 = 1

    max_x = 13
    xs = np.arange(x0, max_x + h, h)
    ys = np.zeros(len(xs))
    ys[0] = y0

    for i, x in enumerate(xs):
        if i == 0:
            continue
        ys[i] = next_step(x - h, ys[i - 1], h)

    print(xs)
    print(ys)
    fine = np.arange(x0, max_x, 0.01)
    plt.plot(fine, exact(fine))
    plt.plot(xs, ys)
    plt.legend(["Exact", "Approximation"])
    plt.grid()
    plt.show()
