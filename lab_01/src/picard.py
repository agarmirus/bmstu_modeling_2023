def fst_picard_1(x: float) -> float:
    return x ** 3 / 3 + x + 1


def snd_picard_1(x: float) -> float:
    return x ** 4 / 12 + x ** 3 / 3 + x * x / 2 + x + 1


def thd_picard_1(x: float) -> float:
    return x ** 5 / 60 + x ** 4 / 48 + x ** 3 / 2 + x * x / 2 + x + 1


def frth_picard_1(x: float) -> float:
    return x ** 6 / 360 + x ** 5 / 240 + x ** 4 / 8 + x ** 3 / 2 + x * x / 2 + x + 1


def fst_picard_2(x: float) -> float:
    return x ** 4 / 4 + x * x / 2 + 0.5


def snd_picard_2(x: float) -> float:
    return x ** 6 / 12 + x ** 4 / 2 + x * x / 2 + 0.5


def thd_picard_2(x: float) -> float:
    return x ** 8 / 48 + x ** 6 / 6 + x ** 4 / 2 + x * x / 2 + 0.5


def frth_picard_2(x: float) -> float:
    return x ** 10 / 240 + x ** 8 / 24 + x ** 6 / 6 + x ** 4 / 2 + x * x / 2 + 0.5


def fst_picard_3(x: float) -> float:
    return x ** 3 / 3


def snd_picard_3(x: float) -> float:
    return x ** 7 / 63 + x ** 3 / 3


def thd_picard_3(x: float) -> float:
    return x ** 15 / 59535 + 2 * x ** 11 / 2079 + x ** 7 / 63 + x ** 3 / 3


def frth_picard_3(x: float) -> float:
    return x ** 31 / 109876902975 + 4 * x ** 27 / 3341878155 + 4 * x ** 23 / 10438212015 + 82 * x ** 19 / 37328445 + \
    13 * x ** 15 / 218295 + 2 * x ** 11 / 2079 + x ** 7 / 63 + x ** 3 / 3
