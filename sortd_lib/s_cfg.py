from configparser import ParsingError, RawConfigParser
from os import linesep
from sys import stdin, stdout

from .consts import ERROR
from .lib import log, recur_sort


class _Parser(RawConfigParser):
    def optionxform(self, optionstr: str) -> str:
        return optionstr


def p_cfg() -> int:
    parser = _Parser(allow_no_value=True, strict=False, interpolation=None)
    try:
        parser.read_file(stdin)
    except ParsingError as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        return 1
    else:
        cfg = recur_sort({**parser})
        parser = _Parser()
        parser.read_dict(cfg)
        parser.write(stdout)
        return 0
