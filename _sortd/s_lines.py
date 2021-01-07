from locale import strxfrm
from os import linesep
from sys import stdin


def p_lines(read0: bool, print0: bool) -> None:
    r_sep = "\0" if read0 else linesep
    w_sep = "\0" if print0 else linesep
    lines = stdin.read().split(r_sep)
    lines.sort(key=strxfrm)
    print(*lines, sep=w_sep, end="")
