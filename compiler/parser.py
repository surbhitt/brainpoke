from lexer import Lexer, Op_kind
from common.memory import Memory

class Parser:
    op_jio = {Op_kind.JMP_IF_Z, Op_kind.JMP_IF_NZ, Op_kind.INP} # op_ JMP I/0
    addr_stck = []
    def __init__(self, l: Lexer):    
        self.operation = None # Op_kind
        self.operand = None   # Operand
        self.inter_repr = []  # intermediate representation
        self.generate_ir(l)
    
    def generate_ir(self, l: Lexer):
        token = l.next()
        # decide if it is operand or operation and 
        # assign values
        self.operand = 1
        while token:
            if token in self.op_jio:
                # check for imbalance in the jmp statement
                if token == Op_kind.JMP_IF_Z:
                    # backpatching
                    self.addr_stck.append(len(self.inter_repr))
                    self.inter_repr.append([token, None])
                elif token == Op_kind.JMP_IF_NZ:
                    idx_jz = self.addr_stck.pop()
                    self.inter_repr.append((token, idx_jz))
                    self.inter_repr[idx_jz][1] = len(self.inter_repr)
                else: # token == Op_kind.INP:
                    inp = l.next()
                    self.inter_repr.append((token, inp))
                token = l.next()
                continue
            
            next_token = l.next()
            if next_token == token:
                self.operand += 1
            else:
                self.inter_repr.append((token, self.operand))
                self.operand = 1
            token = next_token

    def exec_ir_on_mem(self, mem: Memory):
        # set bounds to operations
        # can not acceed memory limit andk one byte memory contraints
        i = 0
        while i < len(self.inter_repr):

            opcode, operand = self.inter_repr[i] 
            if opcode == Op_kind.INC_VAL:
                mem.memory[mem.ptr] += operand
            elif opcode == Op_kind.DEC_VAL:
                mem.memory[mem.ptr] -= operand
            elif opcode == Op_kind.INC_PTR:
                mem.ptr += operand
            elif opcode == Op_kind.DEC_PTR:
                mem.ptr -= operand
            elif opcode == Op_kind.INP:
                mem.memory[mem.ptr] = operand
            elif opcode == Op_kind.OUT:
                while operand:
                    print(chr(mem.memory[mem.ptr]), end="")
                    operand -= 1
            elif opcode == Op_kind.JMP_IF_Z:
                if not mem.memory[mem.ptr]:
                    i = operand - 1
            elif opcode == Op_kind.JMP_IF_NZ:
                if mem.memory[mem.ptr]:
                    i = operand - 1
            i+=1
