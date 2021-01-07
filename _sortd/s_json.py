from json import JSONDecodeError, dump, load
from os import linesep
from sys import stderr, stdin, stdout

from .lib import recur_sort


def p_json(indent: int) -> None:
    try:
        data = load(stdin)
    except JSONDecodeError as e:
        print("Error!", e, sep=linesep, file=stderr)
        exit(1)
    else:
        json = recur_sort(data)
        dump(json, stdout, ensure_ascii=False, check_circular=False, indent=indent)
