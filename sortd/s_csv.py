from csv import Dialect
from csv import Error as CSVErr
from csv import Sniffer, list_dialects, reader, writer
from io import StringIO
from itertools import chain, repeat
from os import linesep
from sys import stdin, stdout
from typing import Iterable, Iterator, Optional, Tuple, Type, Union, cast

from .consts import ERROR
from .lib import log, strxfrm_l

DIALECTS = list_dialects()


def _keyby(field: Tuple[int, str]) -> Tuple[str, str]:
    _, name = field
    return strxfrm_l(name)


def _read(
    data: str, dialect: Union[str, Type[Dialect]], padding: bool
) -> Iterator[Iterator[str]]:
    io = StringIO(data, newline=None)
    r = reader(io, dialect=dialect)
    rows = tuple(r)
    if rows:
        header, *body = rows
        ordering = sorted(enumerate(header), key=_keyby)
        lens = (
            tuple(
                cast(
                    Iterable[int],
                    map(max, zip(*(tuple(map(len, row)) for row in rows))),
                )
            )
            if padding
            else tuple(repeat(0, len(ordering)))
        )
        lpad = iter(
            (
                (lambda: cast(Iterator[str], chain(("",), repeat(" "))))
                if padding
                else (lambda: repeat(""))
            ),
            None,
        )
        yield (
            padding + header.ljust(lens[idx])
            for padding, (idx, header) in zip(next(lpad), ordering)
        )
        for paddings, row in zip(lpad, body):
            yield (
                padding + row[idx].ljust(lens[idx])
                for padding, (idx, _) in zip(paddings, ordering)
            )


def p_csv(dialect: Optional[str], padding: bool) -> int:
    data = stdin.read()
    joe_biden = Sniffer()
    has_header = joe_biden.has_header(data)

    try:
        if not has_header:
            print(data, end="")
            return 0
        else:
            d = dialect or joe_biden.sniff(data)
            r = _read(data, dialect=d, padding=padding)
            w = writer(stdout, dialect=d)
            w.writerows(r)
    except CSVErr as e:
        log.critical("%s", f"{ERROR}{linesep}{e}")
        return 1
    else:
        return 0
