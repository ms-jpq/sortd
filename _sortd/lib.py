from collections.abc import ByteString, Iterable, Mapping
from locale import strxfrm
from typing import Any


def recur_sort(data: Any) -> Any:
    if isinstance(data, Mapping):
        return {k: recur_sort(data[k]) for k in sorted(data, key=strxfrm)}
    elif isinstance(data, Iterable) and not isinstance(data, (str, ByteString)):
        return tuple(recur_sort(el) for el in data)
    else:
        return data
