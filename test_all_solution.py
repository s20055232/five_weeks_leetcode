import os
import subprocess

curr = os.getcwd()

for _dir in os.listdir():
    if _dir.startswith((".", "_")):
        continue
    os.chdir(curr)
    print(_dir)
    os.chdir(_dir)
    subprocess.run(["pytest", "."])
