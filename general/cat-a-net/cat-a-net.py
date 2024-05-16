import os
import sys

sys.path.append(".")

import pwn
from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1]

remote = pwn.remote(host="0.cloud.chals.io", port=28862)

output = remote.recvall()
output = output.decode()

dir = save_flag(output, __file__)