import sys
sys.path.append(".")

from util import *

from Crypto.Util.number import *

FLAG = b'elio{b7t3S_T0_L0N7_4_C4n_C0d3_1n_P4YTH0N}'

print(bytes_to_long(FLAG))

dir = save_flag(FLAG.decode(), __file__)