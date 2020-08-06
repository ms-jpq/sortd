from configparser import ConfigParser, ParsingError
from sys import stderr, stdin, stdout
from typing import Any

from .lib import recur_sort


def load_ini() -> Any:
    parser = ConfigParser()
    try:
        parser.read_file(stdin)
    except ParsingError as e:
        print("Error!", e, sep="\n", file=stderr)
        exit(1)
    else:
        ini = {**parser}
        return recur_sort(ini)


def dump_ini(ini: Any) -> None:
    parser = ConfigParser()
    parser.read_dict(ini)
    parser.write(stdout)
