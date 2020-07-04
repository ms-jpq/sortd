from sys import stderr, stdin, stdout
from typing import Any

from toml import dump, load
from toml.decoder import TomlDecodeError

from .lib import recur_sort


def load_toml() -> Any:
    try:
        toml = load(stdin)
        return recur_sort(toml)
    except TomlDecodeError as e:
        print("Error!", e, sep="\n", file=stderr)
        exit(1)


def dump_toml(toml: Any) -> None:
    dump(toml, stdout)
