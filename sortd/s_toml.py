from sys import stderr, stdin, stdout
from typing import Any

from toml import dump, load
from toml.decoder import TomlDecodeError

from .lib import recur_sort


def load_toml() -> Any:
    try:
        toml = load(stdin)
    except TomlDecodeError as e:
        print("Error!", e, sep="\n", file=stderr)
        exit(1)
    else:
        return recur_sort(toml)


def dump_toml(toml: Any) -> None:
    dump(toml, stdout)
