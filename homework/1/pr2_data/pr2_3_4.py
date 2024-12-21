import os
import sys
import re
from pathlib import Path

MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


def get_argv_dir() -> Path:
    if len(sys.argv) < 2:
        print("Аргумент отстуствует")
        print("В качестве аргумента должен быть путь до папки с файлами. К примеру ./testdirs/testdir")
        exit(1)

    if len(sys.argv) > 2:
        print("Слишком много аргрументов")
        exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print("Данной директории не существует")

    if path.is_file():
        print("Данный путь это файл")
        exit(1)

    if not path.is_dir():
        print("Данный путь не директория")
        exit()

    return path


dir_name = get_argv_dir()

for filename in os.listdir(dir_name):
    if not re.match(f"data-\\d\\d-(?:{"|".join(MONTHS)})-\\d\\d", filename.lower()):
        print(f"Файл \"{filename}\" не соответвует формату \"data-DD-MMM-YY.txt\". Он будет проигнорирован")
        continue

    d, month, y = int(filename[5:7]), filename[8:11], int(filename[12:14])
    m = MONTHS.index(month.lower()) + 1
    newname = 'data-20{:02d}-{:02d}-{:02d}.txt'.format(y, m, d)
    newpath = dir_name / newname
    oldpath = dir_name / filename
    print(oldpath, '->', newpath)
    os.rename(oldpath, newpath)
