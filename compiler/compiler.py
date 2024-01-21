#!/usr/bin/env python3

from sys import argv
from common.memory import Memory
from compiler.lexer import Lexer
from compiler.parser import Parser 

def compiler(source_file_path: str):
    with open(source_file_path, 'r') as source_file:
        l = Lexer(source_file.read())
        ir = Parser(l)
        mem = Memory()
        ir.exec_ir_on_mem(mem)
    

if __name__ == "__main__":
    if len(argv) > 1:
        compiler(argv[1])

