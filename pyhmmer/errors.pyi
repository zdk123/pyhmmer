# coding: utf-8
import typing

from pyhmmer.easel import Alphabet

statuscode: typing.Dict[int, str]

class UnexpectedError(RuntimeError):
    code: int
    function: str
    def __init__(self, code: int, function: str) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class AllocationError(MemoryError):
    ctype: str
    itemsize: int
    count: int
    def __init__(self, ctype: str, itemsize: int, count: int = 1) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class EaselException(RuntimeError):
    code: int
    message: str
    def __init__(self, code: int, message: str) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class AlphabetMismatch(ValueError):
    expected: Alphabet
    actual: Alphabet
    def __init__(self, expected: Alphabet, actual: Alphabet) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...

class ServerError(RuntimeError):
    code: int
    message: str
    def __init__(self, code: int, message: str) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...


class MissingCutoffs(ValueError):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...