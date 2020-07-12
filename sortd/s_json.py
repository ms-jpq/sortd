from json import JSONDecodeError, dump, load
from sys import stderr, stdin, stdout
from typing import Any

from .lib import recur_sort


def load_json() -> Any:
    try:
        json = load(stdin)
        return recur_sort(json)
    except JSONDecodeError as e:
        print("Error!", e, sep="\n", file=stderr)
        exit(1)


def dump_json(json: Any, *, indent: int) -> None:
    dump(json, stdout, ensure_ascii=False, indent=indent)
