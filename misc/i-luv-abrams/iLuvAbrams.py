import os
import sys

sys.path.append(".")

import pwn
from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1]

out, err = run_bash(["cd", cur_dir, "&&", "strings", "main.jpg"])

out = out.splitlines()
hex_val = out[-1]

result = pwn.unhex(hex_val)
result = result.decode()

dir = save_flag(result, __file__)