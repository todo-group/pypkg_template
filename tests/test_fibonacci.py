"""Test pypkg_template.fibonacci module."""

from __future__ import annotations

import pytest

from pypkg_template import fibonacci
from tests.conftest import EXACT

_NAIVE_TOL = 20


def test_ng() -> None:
    """Test with negative n."""
    with pytest.raises(ValueError, match=r"n must be non-negative, got .*\."):
        fibonacci.naive(-1)


@pytest.mark.parametrize(("n", "ref"), EXACT.items())
def test_naive(n: int, ref: int) -> None:
    """Test naive."""
    if n > _NAIVE_TOL:
        pytest.skip("Too slow.")
    assert fibonacci.naive(n) == ref


@pytest.mark.parametrize(("n", "ref"), EXACT.items())
def test_closuredp(n: int, ref: int) -> None:
    """Test closuredp."""
    fib = fibonacci.closuredp()
    assert fib(n) == ref


@pytest.mark.parametrize(("n", "ref"), EXACT.items())
def test_classdp(n: int, ref: int) -> None:
    """Test ClassDP."""
    fib = fibonacci.ClassDP()
    assert fib(n) == ref
