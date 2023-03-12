from euler import *
from picard import *

from analit import analit_1, analit_2


def perform_task_1(e: float, step: float):
    print("Задание 1")
    print(
        "|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
            "Аргумент", "Аналит.", "Эйлер", "1 приб. П.", "2 приб. П.", "3 приб. П.", "4 приб. П."
        )
    )
    print('-' * (16 * 7 + 1))

    prev_x = 0.0
    prev_y = 1.0

    while prev_x < e:
        euler_y = euler_1(prev_y, prev_x, step)

        print(
            "|{:^15.3e}|{:^15.3e}|{:^15.3e}|{:^15.3e}|{:^15.3e}|{:^15.3e}|{:^15.3e}|".format(
                prev_x,
                analit_1(prev_x),
                euler_y,
                fst_picard_1(prev_x),
                snd_picard_1(prev_x),
                thd_picard_1(prev_x),
                frth_picard_1(prev_x)
            )
        )

        prev_y = euler_y
        prev_x += step

    print()


def perform_task_2(e: float, step: float):
    print("Задание 2")
    print(
        "|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
            "Аргумент", "Аналит.", "Эйлер", "1 приб. П.", "2 приб. П.", "3 приб. П.", "4 приб. П."
        )
    )
    print('-' * (16 * 7 + 1))

    prev_x = 0.0
    prev_y = 0.5

    while prev_x < e:
        euler_y = euler_2(prev_y, prev_x, step)

        print(
            "|{:^15.3e}|{:^15.3e}|{:^15.3e}|{:^15.3e}|{:^15.3e}|{:^15.3e}|{:^15.3e}|".format(
                prev_x,
                analit_2(prev_x),
                euler_y,
                fst_picard_2(prev_x),
                snd_picard_2(prev_x),
                thd_picard_2(prev_x),
                frth_picard_2(prev_x)
            )
        )

        prev_y = euler_y
        prev_x += step
        
    print()


def perform_task_3(e: float, step: float):
    print("Задание 3")
    print(
        "|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
            "Аргумент", "Эйлер", "1 приб. П.", "2 приб. П.", "3 приб. П.", "4 приб. П."
        )
    )
    print('-' * (16 * 6 + 1))

    prev_x = 0.0
    prev_y = 0.0

    while prev_x < e:
        euler_y = prev_y + step * (prev_x ** 2 + prev_y ** 2)

        print(
            "|{:^15.6e}|{:^15.6e}|{:^15.6e}|{:^15.6e}|{:^15.6e}|{:^15.6e}|".format(
                prev_x,
                euler_y,
                fst_picard_3(prev_x),
                snd_picard_3(prev_x),
                thd_picard_3(prev_x),
                frth_picard_3(prev_x)
            )
        )

        prev_y = euler_y
        prev_x += step
        
    print()


def main():
    e = float(input("Верхняя граница интервала: "))
    step = float(input("Размер шага: "))

    # perform_task_1(e, step)
    # perform_task_2(e, step)
    perform_task_3(e, step)


if __name__ == "__main__":
    main()
