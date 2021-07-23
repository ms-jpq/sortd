from io import BytesIO
from os import linesep
from plistlib import InvalidFileException, dump, load
from sys import stdin, stdout

from .consts import ERROR
from .lib import log, recur_sort


def p_plist() -> None:
    io = BytesIO(stdin.buffer.read())
    try:
        data = load(io)
    except InvalidFileException as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        exit(1)
    else:
        plist = recur_sort(data)
        dump(plist, stdout.buffer, sort_keys=False)

