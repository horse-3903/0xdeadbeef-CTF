import pwn

import re
import string

import os
import sys

sys.path.append(".")

from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

remote = pwn.remote(host="0.cloud.chals.io", port=23941)
    
output = remote.recv()
print(output, end="\n\n")

remote.sendline(b"1")

output = remote.recv()
print(output, end="\n\n")

remote.sendline(b"0")

output = remote.recv()
print(output, end="\n\n")

output = output.decode()
output = re.search("'(.*?)'", output)

result = output.group(1)

remote.close()

print()

dir = save_flag(result, __file__)