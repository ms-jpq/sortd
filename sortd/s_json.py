from json import JSONDecodeError, dump, load
from sys import stderr, stdin, stdout
from typing import Any

from .lib import recur_sort


def load_json() -> Any:
    try:
        json = load(stdin)
    except JSONDecodeError as e:
        print("Error!", e, sep="\n", file=stderr)
        exit(1)
    else:
        return recur_sort(json)


def dump_json(json: Any, *, indent: int) -> None:
    dump(json, stdout, ensure_ascii=False, check_circular=False, indent=indent)
