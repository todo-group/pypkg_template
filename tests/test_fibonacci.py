"""Test pypkg_template.fibonacci module."""

from __future__ import annotations

from pypkg_template import fibonacci

_NAIVE_TOL = 30


def test_naive(fx_exact: dict[int, int]) -> None:
    """Test naive."""
    for n, ref in fx_exact.items():
        if n > _NAIVE_TOL:
            continue
        assert fibonacci.naive(n) == ref


def test_closuredp(fx_exact: dict[int, int]) -> None:
    """Test closuredp."""
    fib = fibonacci.closuredp()
    for n, ref in fx_exact.items():
        assert fib(n) == ref


def test_classdp(fx_exact: dict[int, int]) -> None:
    """Test ClassDP."""
    fib = fibonacci.ClassDP()
    for n, ref in fx_exact.items():
        assert fib(n) == ref
