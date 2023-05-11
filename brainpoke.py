# make a choice whether i can take the input with the command
class Memory(object):
	def __init__(self):
		self.memory = [0]*3000;
		self.pointer = 0
	
	def memory_as_string(self):
		return str(self.memory)

	def handle_operations(self, operator: chr, operand) -> dict:
		status = {}
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
			if loop_self.pointer[0] == -1:
				loop_self.pointer[0] = self.pointer
			if self.memory[self.pointer] == 0:
				self.pointer = loop_self.pointer[1]
				loop_self.pointer = [-1, -1]
		elif operator == "]":
			loop_self.pointer[1] = self.pointer
			self.pointer = loop_self.pointer[0]"""
		status['0'] = "executed"
		f = open('memory.txt','w')
		f.write(str(self.memory))
		return status
