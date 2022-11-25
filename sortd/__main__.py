from argparse import ArgumentParser, Namespace
from enum import Enum, auto
from shutil import get_terminal_size
from signal import SIG_DFL, SIGPIPE, signal
from typing import NoReturn

from .consts import INDENT
from .s_cfg import p_cfg
from .s_csv import DIALECTS, p_csv
from .s_json import p_json
from .s_lines import p_lines
from .s_plist import p_plist
from .s_toml import p_toml
from .s_yaml import p_yaml


class _Parsers(Enum):
    cfg = auto()
    csv = auto()
    json = auto()
    lines = auto()
    plist = auto()
    toml = auto()
    yaml = auto()


def _parse_args() -> Namespace:
    cols, _ = get_terminal_size((80, -1))

    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers(dest="format", required=True)

    s_cfg = sub_parsers.add_parser(_Parsers.cfg.name)

    s_csv = sub_parsers.add_parser(_Parsers.csv.name)
    s_csv.add_argument("-d", "--dialect", choices=DIALECTS, default=None)
    s_csv.add_argument("-p", "--padding", action="store_true")

    p_json = sub_parsers.add_parser(_Parsers.json.name)
    p_json.add_argument("-i", "--indent", type=int, default=INDENT)

    p_lines = sub_parsers.add_parser(_Parsers.lines.name)
    p_lines.add_argument("--read0", action="store_true")
    p_lines.add_argument("--print0", action="store_true")

    p_plist = sub_parsers.add_parser(_Parsers.plist.name)

    p_toml = sub_parsers.add_parser(_Parsers.toml.name)

    p_yaml = sub_parsers.add_parser(_Parsers.yaml.name)
    p_yaml.add_argument("-i", "--indent", type=int, default=INDENT)
    p_yaml.add_argument("-w", "--width", type=int, default=cols)

    return parser.parse_args()


def _main() -> int:
    signal(SIGPIPE, SIG_DFL)
    args = _parse_args()

    parser = _Parsers[args.format]
    if parser is _Parsers.cfg:
        return p_cfg()

    elif parser is _Parsers.csv:
        return p_csv(dialect=args.dialect, padding=args.padding)

    elif parser is _Parsers.json:
        return p_json(indent=args.indent)

    elif parser is _Parsers.lines:
        return p_lines(read0=args.read0, print0=args.print0)

    elif parser is _Parsers.plist:
        return p_plist()

    elif parser is _Parsers.toml:
        return p_toml()

    elif parser is _Parsers.yaml:
        return p_yaml(width=args.width, indent=args.indent)

    else:
        assert False


def main() -> NoReturn:
    try:
        exit(_main())
    except KeyboardInterrupt:
        exit(130)
    except BrokenPipeError:
        exit(13)


if __name__ == "__main__":
    main()
