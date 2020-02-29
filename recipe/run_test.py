import os
import subprocess
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
    # can't test this, yet, because of pyppeteer_fork
    ["visualization", "n2_viewer", "tests", "test_gui.py"]
]

[
    os.unlink(join(dirname(openmdao.__file__), *tf2d))
    for tf2d in test_files_to_delete
]

sys.exit(subprocess.call([
    "testflo", "--config", ".testflo", "--numprocs", "1", "openmdao", "-v", "--pre_announce"
]))
