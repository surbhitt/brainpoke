#!/usr/bin/env python3
from sys import argv
from gui.interface import interface
from compiler.compiler import compiler
"""
		to do
	1. create a memory view
	2. create a reset
	3. create a history
	4. 

	render the corrent pointer add
	the value inside the mem
"""


def main ():
    if len(argv) > 1:
        compiler(argv[1])
    else:
        print("[INFO] Implementation incomplete")
	    # interface()

if __name__ == '__main__':
	main()
