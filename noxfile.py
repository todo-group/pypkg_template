"""Run nox sessions."""

import nox
from nox import Session


@nox.session
def tests(session: Session) -> None:
    """Run the test suite."""
    session.install("pytest", "pytest-cov")
    # Need to use `-e`
    session.install("-e", ".")
    session.run("pytest", "--cov=src")
