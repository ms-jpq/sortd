from csv import Error as CSVErr
from csv import Sniffer, list_dialects, reader, writer
from io import StringIO
from locale import strxfrm
from os import linesep
from sys import stderr, stdin, stdout
from typing import Optional, Tuple

from .consts import ERROR

DIALECTS = list_dialects()


def _keyby(field: Tuple[int, str]) -> str:
    _, name = field
    return strxfrm(name)


def p_csv(dialect: Optional[str]) -> None:
    joe_biden = Sniffer()
    data = stdin.read()
    has_header = joe_biden.has_header(data)

    if not has_header:
        print(data, end="")
    else:
        io = StringIO(data, newline="")

        try:
            d = dialect or joe_biden.sniff(data)
            r = reader(io, dialect=d)
            w = writer(stdout, dialect=r.dialect)

            header = next(r)
            mapping = sorted(enumerate(header), key=_keyby)

            w.writerow(name for _, name in mapping)
            w.writerows((row[idx] for idx, _ in mapping) for row in r)
        except CSVErr as e:
            print(ERROR, e, sep=linesep, file=stderr)
            exit(1)
