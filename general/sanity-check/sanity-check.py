import os
import sys

sys.path.append(".")

import pwn
from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1]

flag = "elio{sAnt1y_ch3Ck_A1kFK}"

dir = save_flag(flag, __file__)