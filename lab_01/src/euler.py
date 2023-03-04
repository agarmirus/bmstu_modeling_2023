from analit import f1, f2, f3


def euler_1(prev_y: float, prev_x: float, step: float) -> float:
    return prev_y + step * f1(prev_x, prev_y)


def euler_2(prev_y: float, prev_x: float, step: float) -> float:
    return prev_y + step * f2(prev_x, prev_y)


def euler_3(prev_y: float, prev_x: float, step: float) -> float:
    return prev_y + step * f3(prev_x, prev_y)
