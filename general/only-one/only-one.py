import os
import sys

sys.path.append(".")

import base64
from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

out, err = run_bash(["cd", cur_dir, "&&", "cat", "uniq.txt", "|", "sort", "|", "uniq", "-u"])

result = base64.b64decode(out)
result = result.decode()

dir = save_flag(result, __file__)