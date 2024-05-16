flag = "elio{REDACTED}"

encrypted = ""
for char in flag:
    if char in "{}_":
        encrypted += char
    elif char in "0123456789":
        cnt = int(char)
        encrypted += str(9 - cnt)
    else:
        cnt = ord(char) - 96
        cnt = 26 - cnt + 1
        encrypted += chr(cnt + 96)

for i in range(3):
    encrypted = encrypted[::2] + encrypted[1::2]

print(encrypted)

# v8xx5hk2irtm9}ir_t{h__om8lgg8h8l_t8