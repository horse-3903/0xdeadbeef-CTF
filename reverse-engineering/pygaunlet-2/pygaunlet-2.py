import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

from tqdm import tqdm

encrypted = "dmhnzust2^l5462s^1g^qxu51o>^|"
encrypted = [ord(i) for i in encrypted]

for key in tqdm(range(int(1e6))):
    for j in range(len(encrypted)):
        encrypted[j] ^= (key**(j+1)) % 127

    decrypted = "".join([chr(i) for i in encrypted])

    if "elio" in decrypted:
        break

dir = save_flag(decrypted, __file__)