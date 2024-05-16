import subprocess

def save_flag(flag: str, file: str) -> str:
    name = file.split(".")[:-1][-1]
    
    dir = f"{name}-flag.txt"

    flag = flag.strip()

    print(f"Password Found : {flag}\n")

    print(f"Saving password to {dir}", end="...")
    
    with open(dir, "w+") as f:
        f.write(flag)

    print("Done\n")

    return dir

def run_bash(command: list[str]) -> tuple[str, str] | tuple[bytes, bytes]:
    command = " ".join(command)

    print(f"Running bash command : `{command}`", end="...")
    
    p = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out, err = p.communicate(command.encode())

    print("Done\n")
    
    try:
        out, err = out.decode("unicode-escape"), err.decode("unicode-escape")
    except:
        pass

    try:
        out, err = out.decode(), err.decode()
    except:
        pass

    if not err:
        print("Output received : ")
        print(out.strip("\n") or None)
    else:
        print("Error caught : ")
        print(err.strip("\n"))

    print()

    try:
        return out.decode(), err.decode()
    except:
        return out, err