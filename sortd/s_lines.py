from os import linesep
from sys import stdin

from .lib import strxfrm_l


def p_lines(read0: bool, print0: bool) -> int:
    r_sep = "\0" if read0 else linesep
    w_sep = "\0" if print0 else linesep
    lines = stdin.read().split(r_sep)
    lines.sort(key=strxfrm_l)
    print(*lines, sep=w_sep, end="")
    return 0
