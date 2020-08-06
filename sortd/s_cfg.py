from configparser import ConfigParser, ParsingError
from sys import stderr, stdin, stdout
from typing import Any

from .lib import recur_sort


def load_cfg() -> Any:
    parser = ConfigParser()
    try:
        parser.read_file(stdin)
    except ParsingError as e:
        print("Error!", e, sep="\n", file=stderr)
        exit(1)
    else:
        ini = {**parser}
        return recur_sort(ini)


def dump_cfg(cfg: Any) -> None:
    parser = ConfigParser()
    parser.read_dict(cfg)
    parser.write(stdout)
