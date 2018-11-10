import os
import subprocess
from pathlib import Path

from jinja2 import Template


HERE = Path(__file__).parent
ROOT = HERE.parent

ARTIFACTS = ROOT / "_artifacts"
CACHE = ROOT / "_cache"

RECIPE_DIR = ROOT / "recipes"

TEST_DIR = ROOT / "tests"

CONDA_OUT = ARTIFACTS / "conda-bld"
TEST_OUT = ARTIFACTS / "test_output"

# for easy overriding in CI
PY_MIN = os.environ.get("PY_MIN", "3.6")
PY_MAX = os.environ.get("PY_MAX", "3.7")
NODE_MIN = os.environ.get("NODE_MIN", "8")
NODE_MAX = os.environ.get("NODE_MAX", "9")
RF_VERSION = os.environ.get("CADQUERY_VERSION", "1.2.1")
VERSION = os.environ.get("CADLAB_VERSION", "0.7.0")


def run(args, **kwargs):
    """ Probably unneccessary "convenience" wrapper
    """
    p = subprocess.Popen(list(map(str, args)), **kwargs)

    try:
        p.wait()
    except KeyboardInterrupt as err:
        p.kill()
        raise err

    return p.returncode
