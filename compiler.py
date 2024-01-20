#!/usr/bin/env python3

import sys
from lexer import Lexer
from parser import Parser 

def main():
    with open(sys.argv[1], 'r') as source_file:
        l = Lexer(source_file.read())
        Parser(l)
    

if __name__ == "__main__":
    main()
