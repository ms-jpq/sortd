from configparser import ConfigParser
from sys import stdin, stdout
from typing import Any

from .lib import recur_sort


def load_ini() -> Any:
    parser = ConfigParser()
    parser.read_file(stdin)
    ini = {**parser}
    return recur_sort(ini)


def dump_ini(ini: Any) -> None:
    parser = ConfigParser()
    parser.read_dict(ini)
    parser.write(stdout)
