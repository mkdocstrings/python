"""Development tasks."""

from __future__ import annotations

import os
import sys
from contextlib import contextmanager
from importlib.metadata import version as pkgversion
from pathlib import Path
from typing import TYPE_CHECKING

from duty import duty, tools

if TYPE_CHECKING:
    from collections.abc import Iterator

    from duty.context import Context


PY_SRC_PATHS = (Path(_) for _ in ("src", "tests", "duties.py", "scripts"))
PY_SRC_LIST = tuple(str(_) for _ in PY_SRC_PATHS)
PY_SRC = " ".join(PY_SRC_LIST)
CI = os.environ.get("CI", "0") in {"1", "true", "yes", ""}
WINDOWS = os.name == "nt"
PTY = not WINDOWS and not CI
MULTIRUN = os.environ.get("MULTIRUN", "0") == "1"


def pyprefix(title: str) -> str:  # noqa: D103
    if MULTIRUN:
        prefix = f"(python{sys.version_info.major}.{sys.version_info.minor})"
        return f"{prefix:14}{title}"
    return title


@contextmanager
def material_insiders() -> Iterator[bool]:  # noqa: D103
    if "+insiders" in pkgversion("mkdocs-material"):
        os.environ["MATERIAL_INSIDERS"] = "true"
        try:
            yield True
        finally:
            os.environ.pop("MATERIAL_INSIDERS")
    else:
        yield False


@duty
def changelog(ctx: Context, bump: str = "") -> None:
    """Update the changelog in-place with latest commits.

    Parameters:
        bump: Bump option passed to git-changelog.
    """
    ctx.run(tools.git_changelog(bump=bump or None), title="Updating changelog")


@duty(pre=["check-quality", "check-types", "check-docs", "check-api"])
def check(ctx: Context) -> None:
    """Check it all!"""


@duty
def check_quality(ctx: Context) -> None:
    """Check the code quality."""
    ctx.run(
        tools.ruff.check(*PY_SRC_LIST, config="config/ruff.toml"),
        title=pyprefix("Checking code quality"),
    )


@duty
def check_docs(ctx: Context) -> None:
    """Check if the documentation builds correctly."""
    Path("htmlcov").mkdir(parents=True, exist_ok=True)
    Path("htmlcov/index.html").touch(exist_ok=True)
    with material_insiders():
        ctx.run(
            tools.mkdocs.build(strict=True, verbose=True),
            title=pyprefix("Building documentation"),
        )


@duty
def check_types(ctx: Context) -> None:
    """Check that the code is correctly typed."""
    os.environ["MYPYPATH"] = "src"
    ctx.run(
        tools.mypy(*PY_SRC_LIST, config_file="config/mypy.ini"),
        title=pyprefix("Type-checking"),
    )


@duty
def check_api(ctx: Context, *cli_args: str) -> None:
    """Check for API breaking changes."""
    ctx.run(
        tools.griffe.check("mkdocstrings_handlers.python", search=["src"], color=True).add_args(*cli_args),
        title="Checking for API breaking changes",
        nofail=True,
    )


@duty
def docs(ctx: Context, *cli_args: str, host: str = "127.0.0.1", port: int = 8000) -> None:
    """Serve the documentation (localhost:8000).

    Parameters:
        host: The host to serve the docs from.
        port: The port to serve the docs on.
    """
    with material_insiders():
        ctx.run(
            tools.mkdocs.serve(dev_addr=f"{host}:{port}").add_args(*cli_args),
            title="Serving documentation",
            capture=False,
        )


@duty
def docs_deploy(ctx: Context, *, force: bool = False) -> None:
    """Deploy the documentation to GitHub pages.

    Parameters:
        force: Whether to force deployment, even from non-Insiders version.
    """
    os.environ["DEPLOY"] = "true"
    with material_insiders() as insiders:
        if not insiders:
            ctx.run(lambda: False, title="Not deploying docs without Material for MkDocs Insiders!")
        origin = ctx.run("git config --get remote.origin.url", silent=True, allow_overrides=False)
        if "pawamoy-insiders/mkdocstrings-python" in origin:
            ctx.run(
                "git remote add upstream git@github.com:mkdocstrings/python",
                silent=True,
                nofail=True,
                allow_overrides=False,
            )
            ctx.run(
                tools.mkdocs.gh_deploy(remote_name="upstream", force=True),
                title="Deploying documentation",
            )
        elif force:
            ctx.run(
                tools.mkdocs.gh_deploy(force=True),
                title="Deploying documentation",
            )
        else:
            ctx.run(
                lambda: False,
                title="Not deploying docs from public repository (do that from insiders instead!)",
                nofail=True,
            )


@duty
def format(ctx: Context) -> None:
    """Run formatting tools on the code."""
    ctx.run(
        tools.ruff.check(*PY_SRC_LIST, config="config/ruff.toml", fix_only=True, exit_zero=True),
        title="Auto-fixing code",
    )
    ctx.run(tools.ruff.format(*PY_SRC_LIST, config="config/ruff.toml"), title="Formatting code")


@duty
def build(ctx: Context) -> None:
    """Build source and wheel distributions."""
    ctx.run(
        tools.build(),
        title="Building source and wheel distributions",
        pty=PTY,
    )


@duty
def publish(ctx: Context) -> None:
    """Publish source and wheel distributions to PyPI."""
    if not Path("dist").exists():
        ctx.run("false", title="No distribution files found")
    dists = [str(dist) for dist in Path("dist").iterdir()]
    ctx.run(
        tools.twine.upload(*dists, skip_existing=True),
        title="Publishing source and wheel distributions to PyPI",
        pty=PTY,
    )


@duty(post=["build", "publish", "docs-deploy"])
def release(ctx: Context, version: str = "") -> None:
    """Release a new Python package.

    Parameters:
        version: The new version number to use.
    """
    origin = ctx.run("git config --get remote.origin.url", silent=True)
    if "pawamoy-insiders/mkdocstrings-python" in origin:
        ctx.run(
            lambda: False,
            title="Not releasing from insiders repository (do that from public repo instead!)",
        )
    if not (version := (version or input("> Version to release: ")).strip()):
        ctx.run("false", title="A version must be provided")
    ctx.run("git add pyproject.toml CHANGELOG.md", title="Staging files", pty=PTY)
    ctx.run(["git", "commit", "-m", f"chore: Prepare release {version}"], title="Committing changes", pty=PTY)
    ctx.run(f"git tag {version}", title="Tagging commit", pty=PTY)
    ctx.run("git push", title="Pushing commits", pty=False)
    ctx.run("git push --tags", title="Pushing tags", pty=False)


@duty(silent=True, aliases=["cov"])
def coverage(ctx: Context) -> None:
    """Report coverage as text and HTML."""
    ctx.run(tools.coverage.combine(), nofail=True)
    ctx.run(tools.coverage.report(rcfile="config/coverage.ini"), capture=False)
    ctx.run(tools.coverage.html(rcfile="config/coverage.ini"))


@duty
def test(ctx: Context, *cli_args: str, match: str = "", snapshot: str = "report") -> None:
    """Run the test suite.

    Parameters:
        match: A pytest expression to filter selected tests.
        snapshot: Whether to "create", "fix", "trim", or "update" snapshots.
    """
    py_version = f"{sys.version_info.major}{sys.version_info.minor}"
    os.environ["COVERAGE_FILE"] = f".coverage.{py_version}"
    args = list(cli_args)
    if snapshot == "disable" or not snapshot:
        args = ["-n", "auto", "--inline-snapshot=disable"]
    else:
        args = [f"--inline-snapshot={snapshot}"]
    ctx.run(
        tools.pytest(
            "tests",
            config_file="config/pytest.ini",
            select=match,
            color="yes",
        ).add_args(*args),
        title=pyprefix("Running tests"),
    )
