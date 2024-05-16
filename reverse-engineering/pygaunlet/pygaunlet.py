import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

encrypted = "v8xx5hk2irtm9}ir_t{h__om8lgg8h8l_t8"

for i in range(3):
    a, b = encrypted[:len(encrypted)//2+1], encrypted[len(encrypted)//2+1:]
    a, b = [*a], [*b]

    if len(a) > len(b):
        b.append("")

    encrypted = [*zip(a, b)]
    encrypted = [e for sl in encrypted for e in sl]
    encrypted = "".join(encrypted)

    print(encrypted)

result = ""

for char in encrypted:
    if char in "{}_":
        result += char
    elif char in "0123456789":
        cnt = int(char)
        result += str(9 - cnt)
    else:
        cnt = ord(char) - 96
        cnt = 26 - cnt + 1
        result += chr(cnt + 96)
    print(result)

print(result)

dir = save_flag(result, __file__)