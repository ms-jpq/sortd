from json import JSONDecodeError, dump, load
from os import linesep
from sys import stdin, stdout

from .consts import ERROR
from .lib import log, recur_sort


def p_json(indent: int) -> int:
    try:
        data = load(stdin)
    except JSONDecodeError as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        return 1
    else:
        json = recur_sort(data)
        dump(
            json,
            stdout,
            ensure_ascii=False,
            check_circular=False,
            allow_nan=False,
            indent=indent,
        )
        return 0
