from collections.abc import Iterable, Mapping
from locale import strxfrm
from logging import StreamHandler, getLogger
from typing import Any

log = getLogger(__name__)
log.addHandler(StreamHandler())


def recur_sort(data: Any) -> Any:
    if isinstance(data, Mapping):
        return {k: recur_sort(data[k]) for k in sorted(data, key=strxfrm)}
    elif isinstance(data, Iterable) and not isinstance(data, (str, bytes, bytearray)):
        return tuple(recur_sort(el) for el in data)
    else:
        return data
