import sys
import math
from typing import TypedDict


class Coordinates(TypedDict):
    latitude: float
    longitude: float


def get_argv_data() -> tuple[Coordinates, Coordinates]:
    if len(sys.argv) < 2:
        print("Аргументы отстуствуют")
        exit(1)

    if len(sys.argv) < 3:
        print("Отстуствует один из аргументов")
        exit(1)

    if len(sys.argv) > 3:
        print("Слишком много аргументов")
        exit(1)

    arg_1_splited = sys.argv[1].split(",")
    arg_2_splited = sys.argv[2].split(",")

    if len(arg_1_splited) < 2:
        print("В первом аргументе недостаточно или отсутвуют числа с точкой")
        exit(1)

    if len(arg_1_splited) > 2:
        print("В первом аргументе слишком много чисел с точкой")
        exit(1)

    if len(arg_2_splited) < 2:
        print("В втором аргументе недостаточно или отсутвуют числа с точкой")
        exit(1)

    if len(arg_2_splited) > 2:
        print("В втором аргументе слишком много чисел с точкой")
        exit(1)

    try:
        data: tuple[Coordinates, Coordinates] = (
            {
                "latitude": math.radians(float(arg_1_splited[0])),
                "longitude": math.radians(float(arg_1_splited[1])),
            },
            {
                "latitude": math.radians(float(arg_2_splited[0])),
                "longitude": math.radians(float(arg_2_splited[1])),
            }
        )
    except ValueError:
        print("В одном из аргументов присутсвует не число")
        exit(1)

    return data


def haversin(x: float | int):
    return math.sin(x / 2) ** 2


def distance(loc1: Coordinates, loc2: Coordinates, R: float = 6378.1):
    return 2 * R * math.asin(
        math.sqrt(
            haversin(loc2["latitude"] - loc1["latitude"]) + (
                math.cos(loc1["latitude"]) * math.cos(loc2["latitude"]) * haversin(loc2["longitude"] - loc1["longitude"])
            )
        )
    )


data = get_argv_data()
print(f"{int(round(distance(*data), 0))} km")
