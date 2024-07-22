import os
import subprocess
import sys
from os.path import join, dirname

import openmdao

# don't test the code_review stuff
TESTFLO = """[testflo]
numprocs = 2
skip_dirs =
  code_review
"""

with open(".testflo", "w") as fp:
    fp.write(TESTFLO)

test_files_to_delete = [
    # can't test these, yet, because of playwright
    ["visualization", "n2_viewer", "tests", "test_gui.py"],
    ["docs", "openmdao_book", "tests", "test_jupyter_gui_test.py"],
    # needs full cuda
    ["jax", "tests", "test_jax.py"],
    ["utils", "tests", "test_jax_utils.py"],
    ["components", "tests", "test_explicit_func_comp.py"],
    ["components", "tests", "test_implicit_func_comp.py"],
    ["core", "tests", "test_partial_color.py"],
]

[os.unlink(join(dirname(openmdao.__file__), *tf2d)) for tf2d in test_files_to_delete]

sys.exit(
    subprocess.call(
        [
            "testflo",
            "--config",
            ".testflo",
            "--stop",
            "-v",
            "--pre_announce",
            "--numprocs",
            "1",
            "openmdao",
        ]
    )
)
