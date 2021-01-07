from os import linesep
from sys import stderr, stdin, stdout

from toml import dump, load
from toml.decoder import TomlDecodeError

from .lib import recur_sort


def p_toml() -> None:
    try:
        data = load(stdin)
    except TomlDecodeError as e:
        print("Error!", e, sep=linesep, file=stderr)
        exit(1)
    else:
        toml = recur_sort(data)
        dump(toml, stdout)
