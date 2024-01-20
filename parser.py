
from lexer import Lexer


class Parser:
    
    def __init__(self, l: Lexer):    
        self.operation = None # Op_kind
        self.operand = None   # Operand
        self.inter_repr = []  # intermediate representation
        self.generate_ir(l)
        self.handle_operations()
    
    def generate_ir(self, l: Lexer):
        token = l.next()
        # decide if it is operand or operation and 
        # assign values
        self.operand = 1
        while token:
            next_token = l.next()
            if next_token == token:
                self.operand += 1
            else:
                self.inter_repr.append((token, self.operand))
                self.operand = 1
            token = next_token

    def handle_operations(self):
        for op in self.inter_repr:
            print(op)
        # print(self.inter_repr)
        return
        """status = {}
        if self.loop_self:
			self.loop_block.append(operator)

		if operator == ">":
			self.pointer += 1
		elif operator == "<":
			self.pointer -= 1
		elif operator == "+":
			self.memory[self.pointer] += 1
		elif operator == "-":
			if self.memory[self.pointer] - 1 > -1:
				self.memory[self.pointer] -= 1
		elif operator == ",":
			try:
				self.memory[self.pointer] = ord(operand)
			except TypeError:
				status['1'] = "enter only a single character"
				return status 
		elif operator == ".":
			if self.memory[self.pointer] != 0:
				# we need to treat characters and numbers differently
				status['2'] = chr(self.memory[self.pointer])	
			else:
				status['2'] = str(0)    
		elif operator == "[":
			self.loop = True
		elif operator == "]":
			# if !self.loop:
				# print("[ missing")
			# handle the loop here
			if self.memory[self.pointer] == 0:
				self.loop = False
			else:
				self.looper(self.pointer)
		status['0'] = "executed"
		f = open('memory.txt','w')
		f.write(str(self.memory))
		return status"""
