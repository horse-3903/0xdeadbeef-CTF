import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import re
import base64

out, err = run_bash(["cd", cur_dir, "&&", "zsteg", "-a", "main.png"])

pt1 = "ZWxpb3tkT195b3VfCg=="
pt2 = "l!KE_horN3TS}"

pt1 = base64.b64decode(pt1)
pt1 = pt1.decode()

result = pt1.strip("\n") + pt2.strip("\n")

dir = save_flag(result, __file__)