from json import JSONDecodeError, dump, load
from os import linesep
from sys import stdin, stdout

from .consts import ERROR
from .lib import log, recur_sort


def p_json(indent: int) -> None:
    try:
        data = load(stdin)
    except JSONDecodeError as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        exit(1)
    else:
        json = recur_sort(data)
        dump(json, stdout, ensure_ascii=False, check_circular=False, indent=indent)

