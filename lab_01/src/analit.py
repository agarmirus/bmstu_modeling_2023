from math import exp


def f1(x: float, y: float):
    return x * x + y


def f2(x: float, y: float):
    return x ** 3 + 2 * x * y


def f3(x: float, y: float):
    return x * x + y * y


def analit_1(x: float) -> float:
    return 3 * exp(x) - x * x - 2 * x - 2


def analit_2(x: float) -> float:
    return exp(x * x) - 0.5 * x * x - 0.5
