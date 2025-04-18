"""Various ways to calculate the Fibonacci sequence."""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import collections.abc


def _argcheck(n: int) -> None:
    if n < 0:
        msg = f"n must be non-negative, got {n}."
        raise ValueError(msg)


def naive(n: int) -> int:
    """Calculate the nth Fibonacci number using a naive recursive algorithm.

    Parameters
    ----------
    n : `int`
        The index of the Fibonacci number to calculate.

    Returns
    -------
    `int`
        The nth Fibonacci number.
    """
    _argcheck(n)
    if n in {0, 1}:
        return n
    return naive(n - 1) + naive(n - 2)


def closuredp() -> collections.abc.Callable[[int], int]:
    r"""Return a closure that calculates the nth Fibonacci number.

    Returns
    -------
    `collections.abc.Callable`\[\[`int`\], `int`\]
        A closure that calculates the nth Fibonacci number.
    """
    mem = {0: 0, 1: 1}

    def fib_closure(n: int) -> int:
        """Calculate the nth Fibonacci number. Results are memoized.

        Parameters
        ----------
        n : `int`
            The index of the Fibonacci number to calculate.

        Returns
        -------
        `int`
            The nth Fibonacci number.
        """
        _argcheck(n)
        if n not in mem:
            mem[n] = fib_closure(n - 1) + fib_closure(n - 2)
        return mem[n]

    return fib_closure


@dataclasses.dataclass
class ClassDP:
    """A callable class internally memoizing the Fibonacci sequence."""

    _mem: dict[int, int]

    def __init__(self) -> None:
        """Initialize ClassDP."""
        self._mem = {0: 0, 1: 1}

    def __call__(self, n: int) -> int:
        """Calculate the nth Fibonacci number. Results are memoized.

        Parameters
        ----------
        n : `int`
            The index of the Fibonacci number to calculate.

        Returns
        -------
        `int`
            The nth Fibonacci number.
        """
        _argcheck(n)
        if n not in self._mem:
            self._mem[n] = self(n - 1) + self(n - 2)
        return self._mem[n]
