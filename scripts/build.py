import sys

from . import (
    CONDA_OUT,
    RECIPE_DIR,
    PY_MIN,
    PY_MAX,
    NODE_MIN,
    NODE_MAX,
    RF_VERSION,
    VERSION,
    run,
)


def build_conda():
    """ Build some packages (mostly re-arching conda-forge `noarch: python`)
    """
    return run(
        [
            "conda-build",
            ".",
            "--output-folder",
            CONDA_OUT,
            "-c",
            "https://repo.anaconda.com/pkgs/main",
            "-c",
            "https://repo.anaconda.com/pkgs/free",
            "-c",
            "https://conda.anaconda.org/conda-forge",
            "--skip-existing",
            "--python",
            PY_MIN,
        ],
        cwd=str(RECIPE_DIR),
    )


if __name__ == "__main__":
    sys.exit(build_conda())
