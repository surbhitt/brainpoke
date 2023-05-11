class Memory(object):
	
	def __init__(self):
		self.memory = [0]*3000;
		self.pointer = 0

	def viewstate(self):
		print(self.memory)
		
	def handle_operations(self, op):
		pass

def operations_on_array (operation, array: list, pointer: int, loop_pointer: list):
	if operation == ">":
		pointer += 1
	elif operation == "<":
		pointer -= 1
	elif operation == "+":
		array[pointer] += 1
	elif operation == "-":
		if array[pointer] - 1 > -1:
			array[pointer] -= 1
	elif operation == ",":
		try:
			inp = input("\tINPUT CHARACTER __ ")
			array[pointer] = ord(inp)
		except TypeError:
			print("\tenter only a single character")
	elif operation == ".":
		if array[pointer] != 0:
			print(f"\t  {chr(array[pointer])=}   is the char stored at {pointer=} ")
		else:
			print(f"\t  0   is the char stored at {pointer=} ")	  
	elif operation == "[":
		if loop_pointer[0] == -1:
			loop_pointer[0] = pointer
		if array[pointer] == 0:
			pointer = loop_pointer[1]
			loop_pointer = [-1, -1]
	elif operation == "]":
		loop_pointer[1] = pointer
		pointer = loop_pointer[0]
	elif operation == "$$":
		print("\tEXITING")
		pass
	else:
		print("\tTHIS IS UNRECOGNISED COMMAND")
	return array, pointer, loop_pointer

	def handle_operations(self):
		pass
