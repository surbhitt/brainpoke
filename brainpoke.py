class Memory:
	def __init__(self):
		self.memory = [0]*3000;
		self.pointer = 0
		self.loop = False
		self.loop_block = []
	
	def memory_as_string(self):
		return str(self.memory)
	
	def looper(self, pointer):
		pass
		# we have to create something for nested loops 
    
	def handle_operations(self, operator: chr, operand) -> dict:
		status = {}
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
		"""elif operator == "[":
			self.loop = True
		elif operator == "]":
			# if !self.loop:
				# print("[ missing")
			# handle the loop here
			if self.memory[self.pointer] == 0:
				self.loop = False
			else:
				self.looper(self.pointer)"""
		status['0'] = "executed"
		f = open('memory.txt','w')
		f.write(str(self.memory))
		return status
