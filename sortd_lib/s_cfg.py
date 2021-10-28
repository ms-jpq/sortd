from configparser import ConfigParser, ParsingError
from os import linesep
from sys import stdin, stdout

from .consts import ERROR
from .lib import log, recur_sort


def p_cfg() -> int:
    parser = ConfigParser(allow_no_value=True, interpolation=None)
    try:
        parser.read_file(stdin)
    except ParsingError as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        return 1
    else:
        cfg = recur_sort({**parser})
        parser = ConfigParser()
        parser.read_dict(cfg)
        parser.write(stdout)
        return 0
