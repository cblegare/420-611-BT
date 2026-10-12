#!/usr/bin/env -S uv run --script --quiet

# /// script
# dependencies = ["nox[uv]"]
# ///

from __future__ import annotations

import dataclasses
import itertools
import os
import shutil
from pathlib import Path
import subprocess
from typing import TYPE_CHECKING
import tomllib

import nox

if TYPE_CHECKING:
    from collections.abc import Collection

PYTHON_VERSIONS = [
    # "3.11",
    # "3.12",
    # "3.13",
    "3.14"
]
DEFAULT_PYTHON = max(PYTHON_VERSIONS)

REPO_ROOT = Path(__file__).parent.resolve()

BUILD_ROOT = REPO_ROOT / "build"
REPORT_ROOT = BUILD_ROOT / "report"
SRC_ROOT = REPO_ROOT / "src"
DOCS_ROOT = REPO_ROOT / "notesdecours"
TEST_ROOT = REPO_ROOT / "test"
COURSE_ROOT = REPO_ROOT / "cours"
PACKAGE_ROOT = REPO_ROOT / "lib"

nox.options.default_venv_backend = "uv"
nox.options.parallel = True


@nox.session(python=DEFAULT_PYTHON, tags=["rst", "format"])
def format_rst(session: nox.Session):
    session.install("git+https://github.com/LilSpazJoekp/docstrfmt.git")
    session.run("docstrfmt",
                "--center-section-titles",
                "--bullet-list-marker",
                "*",
                "--line-length",
                "80",
                "--ordered-marker",
                "1",
                "--section-adornments",
                "#*|=-~'",
                "--custom-directive",
                "index",
                "--indent-width",
                "4",
                DOCS_ROOT)


@nox.session(python=DEFAULT_PYTHON, tags=["rst", "build"])
def build_pdf(session: nox.Session):
    session.run_install(
        "uv",
        "sync",
        f"--project={DOCS_ROOT}",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )

    if not DOCS_ROOT.exists():
        session.skip("No suitable target paths found")

    output_file = sphinx_build(
        session,
        sourcedir=DOCS_ROOT,
        pipeline="latexpdf",
        session_name="420-611-BT-notesdecours"
    )

    shutil.copy(output_file, DOCS_ROOT.joinpath("_static/420-611-BT-notesdecours.pdf"))

    session.log(output_file)

@nox.session(python=DEFAULT_PYTHON, tags=["rst", "build"])
def build_html(session: nox.Session):
    session.run_install(
        "uv",
        "sync",
        f"--project={DOCS_ROOT}",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )

    if not DOCS_ROOT.exists():
        session.skip("No suitable target paths found")

    output_file = sphinx_build(
        session,
        sourcedir=DOCS_ROOT,
        pipeline="html",
        session_name="420-611-BT-notesdecours"
    )

    session.log(output_file)


def sphinx_build(
    session: nox.Session,
    sourcedir: Path | str = DOCS_ROOT,
    outputdir: Path | str | None = None,
    build_root: Path | str = BUILD_ROOT,
    session_name: str = "sphinx",
    pipeline: str = "html",
    write_all: bool = False,
    fresh_env: bool = False,
    tags: Collection[str] | None = None,
    doctrees_dir: Path | str | None = None,
    warning_file: Path | str | None = None,
    jobs: int | None = None,
    conf_dir: Path | str | None = None,
    isolated: bool = False,
    defines: dict[str, str] | None = None,
    html_defines: dict[str, str] | None = None,
    nitpicky: bool = True,
    no_color: bool = False,
    color: bool = False,
    verbose: bool = False,
    quiet: bool = False,
    silent: bool = False,
    fail_on_warning: bool = True,
    keep_going: bool = True,
    show_traceback: bool = True,
    pdb: bool = False,
    exception_on_warning: bool = False,
) -> Collection[Path | str]:
    """
    Make the sphinx command line.

    Requires Sphinx 8.1.
    """

    _build_root = Path(build_root)

    outputdir = outputdir or BUILD_ROOT.joinpath(f"sphinx/{session_name}")
    outputdir.mkdir(parents=True, exist_ok=True)

    doctrees_dir = doctrees_dir or BUILD_ROOT.joinpath(f"doctrees/{session_name}")
    doctrees_dir.mkdir(parents=True, exist_ok=True)

    tags = tags or ()
    _jobs = jobs or "auto"
    defines = defines or {}
    html_defines = html_defines or {}
    outputdir = outputdir or _build_root / session_name

    command = tuple(
        str(part)
        for part in (
            "python",
            "-m",
            "sphinx",
            # Posargs
            "-M",
            pipeline,
            sourcedir,
            outputdir,
            # Flags
            *(("--write-all",) if write_all else ()),
            *(("--fresh-env",) if fresh_env else ()),
            *(("--nitpicky",) if nitpicky else ()),
            *(("--no-color",) if no_color else ()),
            *(("--color",) if color else ()),
            *(("--verbose",) if verbose else ()),
            *(("--quiet",) if quiet else ()),
            *(("--silent",) if silent else ()),
            *(("--fail-on-warning",) if fail_on_warning else ()),
            *(("--keep-going",) if keep_going else ()),
            *(("--show-traceback",) if show_traceback else ()),
            *(("--pdb",) if pdb else ()),
            *(("--exception-on-warning",) if exception_on_warning else ()),
            # Kwargs
            "--jobs",
            _jobs,
            *(("--conf-dir", conf_dir) if conf_dir else ()),
            *(("--doctree-dir", doctrees_dir) if doctrees_dir else ()),
            *(("--warning-file", warning_file) if warning_file else ()),
            *(("--isolated",) if isolated else ()),
            # Multi kwargs
            *itertools.chain(("--tag", tag) for tag in tags),
            "--tag", pipeline,
            *itertools.chain(
                ("--define", f"{key}={value}") for key, value in defines.items()
            ),
            *itertools.chain(
                ("--html-define", f"{key}={value}")
                for key, value in html_defines.items()
            ),
        )
    )
    session.run(*command)

    match pipeline:
        case "html":
            built = outputdir / "index.html"
        case "latexpdf":
            for tex_file in outputdir.glob("latex/*.pdf"):
                built = tex_file
                break
            else:
                session.error(f"Could not find built file in {outputdir}.")

    return built


if __name__ == "__main__":
    nox.main()
