from locale import strxfrm
from signal import SIG_DFL, SIGPIPE, signal
from typing import Any


def sig_trap() -> None:
    signal(SIGPIPE, SIG_DFL)


def recur_sort(data: Any) -> Any:
    if type(data) is dict:
        return {k: recur_sort(data[k]) for k in sorted(data, key=strxfrm)}
    elif type(data) is list:
        return [recur_sort(el) for el in data]
    else:
        return data
