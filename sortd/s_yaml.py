#!/usr/bin/env python3

from sys import stderr, stdin, stdout
from typing import Any, Callable

from yaml import BaseDumper, SafeDumper, add_representer, safe_dump_all, safe_load_all
from yaml.nodes import ScalarNode
from yaml.scanner import ScannerError

from .lib import recur_sort


def repr_str(break_pt: int) -> Callable[[BaseDumper, str], ScalarNode]:
    def repr_str(dumper: BaseDumper, data: str) -> ScalarNode:
        style = ">" if len(data) > break_pt else ""
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)

    return repr_str


def load_yaml() -> Any:
    try:
        yaml = [*safe_load_all(stdin)]
    except ScannerError as e:
        print("Error!", e, sep="\n", file=stderr)
        exit(1)
    else:
        return recur_sort(yaml)


def dump_yaml(yaml: Any, *, width: int, indent: int) -> None:
    fold_pt = width // 2
    add_representer(str, repr_str(fold_pt), Dumper=SafeDumper)
    safe_dump_all(
        yaml,
        stdout,
        allow_unicode=True,
        explicit_start=True,
        width=width,
        indent=indent,
    )
