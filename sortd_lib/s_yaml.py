from os import linesep
from sys import stdin, stdout
from typing import Callable

from yaml import SafeDumper, add_representer, safe_dump_all, safe_load_all
from yaml.nodes import Node, ScalarNode
from yaml.scanner import ScannerError

from .consts import ERROR
from .lib import log, recur_sort


def _repr_str(break_pt: int) -> Callable[[SafeDumper, str], Node]:
    def repr_str(dumper: SafeDumper, data: str) -> ScalarNode:
        if len(data.splitlines()) > 1:
            style = "|"
        elif len(data) > break_pt:
            style = ">"
        else:
            style = ""
        node: ScalarNode = dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style=style
        )
        return node

    return repr_str


def p_yaml(width: int, indent: int) -> int:
    try:
        data = safe_load_all(stdin)
    except ScannerError as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        return 1
    else:
        yaml = recur_sort(data)
        fold_pt = width // 2
        add_representer(str, _repr_str(fold_pt), Dumper=SafeDumper)
        safe_dump_all(
            yaml,
            stdout,
            sort_keys=False,
            allow_unicode=True,
            explicit_start=True,
            width=width,
            indent=indent,
        )
        return 0
