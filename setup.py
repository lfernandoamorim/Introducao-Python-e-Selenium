import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["selenium"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Tutorial-Automacao-Web-com-Python",
    version = "0.1",
    description = "Ele abre um site!", 
    options = {"build_exe": build_exe_options},
    executables = [Executable("Tutorial-Automacao-Web-com-Python.py", base=base)]
)

