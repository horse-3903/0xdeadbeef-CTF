import os
import pwn

import base64

import sys

sys.path.append(".")

from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

remote = pwn.remote(host="0.cloud.chals.io", port=23941)

output = remote.recv()
output = output.decode()
print(output, end="\n\n")

remote.sendline(b"2")

output = remote.recv()
output = output.decode()
print(output, end="\n")

remote.sendline(b"-1")

output = remote.recv()
output = output.decode()
print(output, end="\n\n")

content = output.split(": ")[-1]
content = base64.b64decode(content)
content = content.decode()

print(content)

rot13 = str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
content = content.translate(rot13)

print(content)

print()

dir = save_flag(content, __file__)