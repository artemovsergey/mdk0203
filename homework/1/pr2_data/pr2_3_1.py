import sys

from typing import Generator, Literal


def hailstone_sequence(n: int = 1) -> Generator[int, None, Literal[1]]:
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        yield n
    return n


def get_argv_number() -> int:
    if len(sys.argv) < 2:
        print("Аргумент отстуствует")
        exit(1)

    if len(sys.argv) > 2:
        print("Слишком много аргрументов")
        exit(1)

    arg = sys.argv[1]

    if not arg.isdecimal():
        print("Аргумент не является целым положительным числом")
        exit(1)

    if int(arg) <= 1:
        print("Число не может быть меньше или равняться 1")
        exit(1)

    return int(arg)


num = get_argv_number()

print(f"Последовательность чисел-градин для числа {num}:")

gen = hailstone_sequence(num)

print(next(gen), end="")

try:
    while number := next(gen):
        print(f", {number}", end="")
except StopIteration:
    pass

print()
