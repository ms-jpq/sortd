from configparser import RawConfigParser, ParsingError
from os import linesep
from sys import stdin, stdout

from .consts import ERROR
from .lib import log, recur_sort


def p_cfg() -> int:
    parser = RawConfigParser(allow_no_value=True, strict=False, interpolation=None)
    try:
        parser.read_file(stdin)
    except ParsingError as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        return 1
    else:
        cfg = recur_sort({**parser})
        parser = RawConfigParser()
        parser.read_dict(cfg)
        parser.write(stdout)
        return 0
