import datetime

from typing import Callable, Any

from . import _dias_uteis as dus

_CONTRACT_LETTERS_MONTH = {
    "F": 1,
    "G": 2,
    "H": 3,
    "J": 4,
    "K": 5,
    "M": 6,
    "N": 7,
    "Q": 8,
    "U": 9,
    "V": 10,
    "X": 11,
    "Z": 12,
}


def _verify_ticker(ticker: str):
    if len(ticker) != 6:
        raise ValueError(f"ticker length must be 6, got {len(ticker)}")

    if ticker[:3] != "DI1":
        raise ValueError("ticker needs to start with 'DI1', got {ticker[:3]}")

    if ticker[3] not in _CONTRACT_LETTERS_MONTH.keys():
        raise ValueError(f"invalid ticker contract letter: {ticker[3]}")

    if not ticker[-2:].isdigit():
        raise ValueError(f"expected 2 digits at the end of ticker, got {ticker[-2:]}")


def verify_ticker(func: Callable[[Any], Any]):
    def wrapper(ticker, *args, **kwargs):
        _verify_ticker(ticker)
        return func(ticker, *args, **kwargs)

    return wrapper
