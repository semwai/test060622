import subprocess
from typing import Sequence


def write(filename: str) -> None:
    try:
        f = open(filename, 'w')
        subprocess.run(['driverquery'], stdout=f)
    except FileNotFoundError:
        exit("Can't find 'driverquery' command")


def read(filename: str) -> Sequence[str]:
    with open(filename, 'r', encoding='IBM866') as f:
        return f.readlines()


def filter(data: Sequence[str]) -> Sequence[str]:
    thead = data[2]
    index = thead.index(' ' + thead.split(' ')[2] + ' ')
    return [s for s in data if 'File System' in s[index:]]


def names(data: Sequence[str]) -> Sequence[str]:
    return [s.split(' ')[0] for s in data]