import os
import sys

sys.path.append(".")

import pwn
from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = f".{cur_dir.split('0xdeadbeef CTF')[-1]}/"

out, err = run_bash(["cd", cur_dir, "&&", "sha256sum", "./drop-in/files/*"])

with open(cur_dir+"checksum.txt", "r") as f:
    checksum = f.read()

out, err = run_bash(["cd", cur_dir, "&&", "sha256sum", "./drop-in/files/*", "|", "grep", checksum])

checksum, file = out.split()
file = file.split("files/")[-1]

out, err = run_bash(["cd", cur_dir, "&&", "./decrypt.sh", f"files/{file}"])

