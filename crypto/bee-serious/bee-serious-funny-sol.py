import os
import sys

from collections import Counter

sys.path.append(".")

from util import *
import string

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

with open(cur_dir + "encoded.txt", "r") as f:
    encoded = f.read()

with open(cur_dir + "decoded.txt", "r") as f:
    decoded = f.read()

encoded = [e.upper() for e in encoded if e.isalpha()]
decoded = [d.upper() for d in decoded if d.isalpha()]

key = {s: None for s in string.ascii_uppercase}

for i in range(len(encoded)):
    key[encoded[i]] = decoded[i]

final = ""

with open(cur_dir + "encoded.txt", "r") as f:
    content = f.read()

for c in content:
    if c.isalpha():
        if c.isupper():
            final += key[c]
        else:
            final += key[c.upper()].lower()
    else:
        final += c

with open(cur_dir + "decoded1.txt", "w+") as f:
    f.write(final)

result = final.splitlines()[-1]
result = final.split()[-1]

dir = save_flag(result, __file__)