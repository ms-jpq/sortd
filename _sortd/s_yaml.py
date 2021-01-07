from os import linesep
from sys import stderr, stdin, stdout
from typing import Callable

from yaml import BaseDumper, SafeDumper, add_representer, safe_dump_all, safe_load_all
from yaml.nodes import ScalarNode
from yaml.scanner import ScannerError

from .lib import recur_sort


def repr_str(break_pt: int) -> Callable[[BaseDumper, str], ScalarNode]:
    def repr_str(dumper: BaseDumper, data: str) -> ScalarNode:
        style = ">" if len(data) > break_pt else ""
        node: ScalarNode = dumper.represent_scalar(  # type: ignore
            "tag:yaml.org,2002:str", data, style=style
        )
        return node

    return repr_str


def p_yaml(width: int, indent: int) -> None:
    try:
        data = safe_load_all(stdin)
    except ScannerError as e:
        print("Error!", e, sep=linesep, file=stderr)
        exit(1)
    else:
        yaml = recur_sort(data)
        fold_pt = width // 2
        add_representer(str, repr_str(fold_pt), Dumper=SafeDumper)  # type: ignore
        safe_dump_all(
            yaml,
            stdout,
            allow_unicode=True,
            explicit_start=True,
            width=width,
            indent=indent,
        )
