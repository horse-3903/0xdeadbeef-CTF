import os
import sys

sys.path.append(".")

import pwn
from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1]

remote = pwn.remote(host="0.cloud.chals.io", port=27785)

output = remote.recvall()
output = output.decode()

with open(cur_dir+"/content.txt", "w+") as f:
    f.write(output)

out, err = run_bash(["cd", cur_dir, "&&", "cat", "content.txt", "|", "grep", "^elio{"])

dir = save_flag(out, __file__)