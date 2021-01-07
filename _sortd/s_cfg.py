from configparser import ConfigParser, ParsingError
from os import linesep
from sys import stderr, stdin, stdout

from .lib import recur_sort


def p_cfg() -> None:
    parser = ConfigParser()
    try:
        parser.read_file(stdin)
    except ParsingError as e:
        print("Error!", e, sep=linesep, file=stderr)
        exit(1)
    else:
        cfg = recur_sort({**parser})
        parser = ConfigParser()
        parser.read_dict(cfg)
        parser.write(stdout)
