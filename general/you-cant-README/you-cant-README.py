import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import base64

out, err = run_bash(["cd", cur_dir, "&&", "strings", "readme.txt", "|", "sort", "|", "uniq", "-u"])

result = base64.b64decode(out)
result = result.decode()

result = base64.b64decode(result)
result = result.decode()

dir = save_flag(result, __file__)