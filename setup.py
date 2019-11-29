import cx_Freeze
import sys
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Mi air\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tcl8.6" #you need to ubicate the library where tcl\tcl8.6 is
os.environ['TK_LIBRARY'] = "C:\\Users\\Mi air\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tk8.6" #you need to ubicate the library where tcl\tk8.6 is

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("UImain.py", base=base)]

cx_Freeze.setup(
name = "Vtext",
options = {"build_exe": {"packages":["tkinter"]}},
version = "1.0",
description = "Messenger",
executables = executables
)
