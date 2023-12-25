import os
import subprocess
from pathlib import Path

curr = os.getcwd()

for _dir in os.listdir():
    if _dir.startswith((".", "_")):
        continue
    if not (Path(curr) / _dir).is_dir():
        continue
    os.chdir(curr)
    print(_dir)
    os.chdir(_dir)
    subprocess.run(["pytest", "."])
