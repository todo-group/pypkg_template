"""Various ways to calculate the Fibonacci sequence."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def _argcheck(n: int) -> None:
    if n < 0:
        msg = f"n must be >=0, got {n}."
        raise ValueError(msg)


def naive(n: int) -> int:
    """Calculate the nth Fibonacci number using a naive recursive algorithm.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to calculate.
    """
    _argcheck(n)
    if n in (0, 1):
        return n
    return naive(n - 1) + naive(n - 2)


def closuredp() -> Callable[[int], int]:
    """Return a closure that calculates the nth Fibonacci number."""
    mem = {0: 0, 1: 1}

    def fib_closure(n: int) -> int:
        """Calculate the nth Fibonacci number. Results are memoized.

        Parameters
        ----------
        n : int
            The index of the Fibonacci number to calculate.
        """
        _argcheck(n)
        if n not in mem:
            mem[n] = fib_closure(n - 1) + fib_closure(n - 2)
        return mem[n]

    return fib_closure


class ClassDP:
    """A callable class internally memoizing the Fibonacci sequence."""

    def __init__(self) -> None:
        """Initialize ClassDP."""
        self.__mem = {0: 0, 1: 1}

    def __call__(self, n: int) -> int:
        """Calculate the nth Fibonacci number. Results are memoized.

        Parameters
        ----------
        n : int
            The index of the Fibonacci number to calculate.
        """
        _argcheck(n)
        if n not in self.__mem:
            self.__mem[n] = self(n - 1) + self(n - 2)
        return self.__mem[n]
