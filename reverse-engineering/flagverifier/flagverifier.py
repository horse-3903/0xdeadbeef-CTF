import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import random

random.seed(69)

flag = chr(0x3f - random.randint(-42, 42)) + chr(0x4e - random.randint(-42, 42)) + chr(0x54 - random.randint(-42, 42)) + chr(0x4d - random.randint(-42, 42)) + chr(0x9e - random.randint(-42, 42)) + chr(0x74 - random.randint(-42, 42)) + chr(0x32 - random.randint(-42, 42)) + chr(0x92 - random.randint(-42, 42)) + chr(0x3e - random.randint(-42, 42)) + chr(0x83 - random.randint(-42, 42)) + chr(0x41 - random.randint(-42, 42)) + chr(0x51 - random.randint(-42, 42)) + chr(0x6d - random.randint(-42, 42)) + chr(0x4b - random.randint(-42, 42)) + chr(0x6d - random.randint(-42, 42)) + chr(0x84 - random.randint(-42, 42)) + chr(0x4d - random.randint(-42, 42)) + chr(0x7c - random.randint(-42, 42)) + chr(0x1b - random.randint(-42, 42)) + chr(0x3d - random.randint(-42, 42)) + chr(0x7a - random.randint(-42, 42)) + chr(0xf - random.randint(-42, 42)) + chr(0x79 - random.randint(-42, 42)) + chr(0x61 - random.randint(-42, 42)) + chr(0x47 - random.randint(-42, 42)) + chr(0x61 - random.randint(-42, 42)) + chr(0x1c - random.randint(-42, 42)) + chr(0x6b - random.randint(-42, 42)) + chr(0x55 - random.randint(-42, 42)) + chr(0x5a - random.randint(-42, 42)) + chr(0x83 - random.randint(-42, 42)) + chr(0x6d - random.randint(-42, 42))

dir = save_flag(flag, __file__)