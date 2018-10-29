import os
import subprocess
from pathlib import Path

from jinja2 import Template


HERE = Path(__file__).parent
ROOT = HERE.parent

CONSTRUCT_DIR = ROOT / "constructor"
RECIPE_DIR = ROOT / "recipes"

CONSTRUCT_IN = Template((CONSTRUCT_DIR / "construct.yaml.in").read_text())
CONSTRUCT_CACHE = ROOT / "cache" / "constructor"
CONSTRUCT = CONSTRUCT_DIR / "construct.yaml"

TEST_DIR = ROOT / "tests"

ARTIFACTS = ROOT / "build_artifacts"
CONDA_OUT = ARTIFACTS / "conda-bld"
CONSTRUCT_OUT = ARTIFACTS / "constructor"
TEST_OUT = ARTIFACTS / "tests"

# for easy overriding in CI
PY_MIN = os.environ.get("PY_MIN", "3.6")
PY_MAX = os.environ.get("PY_MAX", "3.7")
NODE_MIN = os.environ.get("NODE_MIN", "8")
NODE_MAX = os.environ.get("NODE_MAX", "9")


def run(args, **kwargs):
    """ Probably unneccessary "convenience" wrapper
    """
    p = subprocess.Popen(args, **kwargs)

    try:
        p.wait()
    except KeyboardInterrupt as err:
        p.kill()
        raise err

    return p.returncode
