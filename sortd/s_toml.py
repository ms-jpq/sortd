from os import linesep
from sys import stdin, stdout

from toml import dump, load
from toml.decoder import TomlDecodeError

from .consts import ERROR
from .lib import log, recur_sort


def p_toml() -> int:
    try:
        data = load(stdin)
    except TomlDecodeError as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        return 1
    else:
        toml = recur_sort(data)
        dump(toml, stdout)
        return 0

