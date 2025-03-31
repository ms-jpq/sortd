from collections.abc import Iterable, Mapping
from locale import strxfrm
from logging import StreamHandler, getLogger
from typing import Any, Tuple

log = getLogger(__name__)
log.addHandler(StreamHandler())


def strxfrm_l(s: str) -> Tuple[str, str]:
    x = strxfrm(s)
    return (x.casefold(), x)


def recur_sort(data: Any) -> Any:
    if isinstance(data, Mapping):
        return {k: recur_sort(data[k]) for k in sorted(data, key=strxfrm_l)}
    elif isinstance(data, Iterable) and not isinstance(data, (str, bytes, bytearray)):
        return tuple(recur_sort(el) for el in data)
    else:
        return data
