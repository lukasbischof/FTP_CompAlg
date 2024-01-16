# vim: set syntax=python:
# -*- coding: utf-8 -*-
#
# Solve the ordinary differential equation y' = x*y^(1/3) with y(1) = 1 using
# the classical Runge-Kutta method with step size h = 0.1
#


import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 0.1
a = 1
b = 3
x = np.arange(a, b + h, h)
y = np.zeros(len(x))
y[0] = 1


def f(x, y):
    return x * y**(1 / 3)


def k1(x, y):
    return h * f(x, y)


def k2(x, y):
    return h * f(x + h / 2, y + k1(x, y) / 2)


def k3(x, y):
    return h * f(x + h / 2, y + k2(x, y) / 2)


def k4(x, y):
    return h * f(x + h, y + k3(x, y))


def exact(x):
    return ((x**2 + 2) / 3)**(3 / 2)


if __name__ == "__main__":
    # Calculate approximate solution using Runge-Kutta method
    for i in range(1, len(x)):
        y[i] = y[i - 1] + (k1(x[i - 1], y[i - 1]) + 2 * k2(x[i - 1], y[i - 1]) +
                           2 * k3(x[i - 1], y[i - 1]) + k4(x[i - 1], y[i - 1])) / 6

    for i in range(len(x)):
        print("x = {:.1f}, y = {:.10f}".format(x[i], y[i]))

    # Calculate the global error of the first two steps (according to the exercise)
    errors = np.abs(y[0:3] - exact(x[0:3]))
    # Print global error in scientific notation
    print("Global error: {:.2e}".format(np.max(errors)))

    # Plot approximate solution and exact solution
    plt.plot(x, y, 'o')
    plt.plot(x, exact(x), 'r--')

    # Plot normalised slope field
    x = np.linspace(a - h, b + h, 20)
    y = np.linspace(0, 7, 20)
    X, Y = np.meshgrid(x, y)
    U = 1
    V = f(X, Y)
    U = U / np.sqrt(U**2 + V**2)
    V = V / np.sqrt(U**2 + V**2)
    plt.quiver(X, Y, U, V, angles='xy', color='lightgray')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['Runge-Kutta', 'Exact'])
    plt.grid(True)
    # plt.show()
