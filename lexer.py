from enum import Enum
# create a class of operations
# is valid can be a function 

class Token_kind(str, Enum):
    OPCODE = 0
    OPERND = 1

class Op_kind(str, Enum):
    INC_VAL = '+' 
    DEC_VAL = '-'
    INC_PTR = '>'
    DEC_PTR = '<'
    JMP_IF_Z = '['
    JMP_IF_NZ = ']'
    INP = ','
    OUT = '.'

    @classmethod
    def is_valid_op(cls, op: str) -> bool:
        for valid_op in Op_kind:
            if op == valid_op:
                return True
        return False

class Lexer:
    # is_valid_token
    # should consider a valid operation 
    # or if prev operation was input
    # a valid literal
    def is_valid_token(self, op):
        return Op_kind.is_valid_op(op) # && should check operand ??
    
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.source_size = len(source)
    
    def next(self):
        # manage operand return
        while (self.pos < self.source_size) and not self.is_valid_token(self.source[self.pos]):
            self.pos+=1
        if self.pos >= self.source_size:
            return None
        token_next = self.source[self.pos]
        self.pos+=1
        # properly send the 
        return token_next # Token_kind.OPCODE


