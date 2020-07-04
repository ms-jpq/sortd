from locale import strxfrm
from sys import stdin
from typing import List


def load_lines(*, nul_term: bool) -> List[str]:
    sep = "\0" if nul_term else "\n"
    lines: List[str] = stdin.read().split(sep)
    lines.sort(key=strxfrm)
    return lines


def dump_lines(lines: List[str], *, nul_term: bool) -> None:
    sep = "\0" if nul_term else "\n"
    print(*lines, sep=sep, end="")
