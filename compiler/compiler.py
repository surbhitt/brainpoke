#!/usr/bin/env python3

import sys
from ..memory import Memory
from lexer import Lexer
from parser import Parser 

def main():
    with open(sys.argv[1], 'r') as source_file:
        mem = Memory()
        l = Lexer(source_file.read())
        ir = Parser(l)
        ir.exec_ir_on_mem(mem)
    

if __name__ == "__main__":
    main()

