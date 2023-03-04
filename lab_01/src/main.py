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

    prev_x = 0.0
    prev_y = 1.0
    i = 0.0
    while i < e + step:
        euler_y = euler_1(prev_y, prev_x, step)

        print(
            "|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|".format(
                i,
                analit_1(i),
                euler_y,
                fst_picard_1(i),
                snd_picard_1(i),
                thd_picard_1(i),
                frth_picard_1(i)
            )
        )

        prev_y = euler_y
        prev_x = i
        i += step

    print()


def perform_task_2(e: float, step: float):
    print("Задание 2")
    print(
        "|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
            "Аргумент", "Аналит.", "Эйлер", "1 приб. П.", "2 приб. П.", "3 приб. П.", "4 приб. П."
        )
    )

    prev_x = 0.0
    prev_y = 0.5
    i = 0.0
    while i < e + step:
        euler_y = euler_2(prev_y, prev_x, step)

        print(
            "|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|".format(
                i,
                analit_2(i),
                euler_y,
                fst_picard_2(i),
                snd_picard_2(i),
                thd_picard_2(i),
                frth_picard_2(i)
            )
        )

        prev_y = euler_y
        prev_x = i
        i += step
        
    print()


def perform_task_3(e: float, step: float):
    print("Задание 2")
    print(
        "|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|".format(
            "Аргумент", "Эйлер", "1 приб. П.", "2 приб. П.", "3 приб. П.", "4 приб. П."
        )
    )

    prev_x = 0.0
    prev_y = 0.0
    i = 0.0
    while i < e + step:
        euler_y = euler_3(prev_y, prev_x, step)

        print(
            "|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|{:^15.3f}|".format(
                i,
                euler_y,
                fst_picard_3(i),
                snd_picard_3(i),
                thd_picard_3(i),
                frth_picard_3(i)
            )
        )

        prev_y = euler_y
        prev_x = i
        i += step
        
    print()


def main():
    e = float(input("Верхняя граница интервала: "))
    step = int(input("Количество шагов: "))

    perform_task_1(e, step)
    perform_task_2(e, step)
    perform_task_3(e, step)


if __name__ == "__main__":
    main()
