import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import string

encode_t = "wrnkesuicjlvbtpaqfoxhgzymd"
decode_t = string.ascii_lowercase

table = str.maketrans(encode_t, decode_t)

encrypted = "evcp{s1uhf3k_0h7_5h8ox17hxc0t?_t1n3_0t3}"
decrypted = encrypted.translate(table)

result = decrypted

dir = save_flag(result, __file__)