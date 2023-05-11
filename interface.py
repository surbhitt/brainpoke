import curses
from brainpoke import Memory


def cmd_view(screen):
	header = """
	Th1s i$ hte brainpoke program
	implement@tion of the brainf**k in python

	=========================================
	| > | move the pntr to rt mem add       |
	| < | move the pntr to lft mem add      |
	| + | inc cur mem add                   |
	| - | dec cur mem add                   |
	| . | out cur mem add                   |
	| , | in cur mem add                    |
	| [ | move to ], if cur mem add holds 0 |
	| ] | move to [                         |   
	=========================================
	"""
	screen.addstr(1, 1, header)

def memory_map(screen):
	# create segment wise rendering of the memory map 
	# with pages, p and n
	# screen.addstr(Memory.memory)
	pass

"""
def handle_commands(op: chr):
	intro2 = '\ton ? prompt enter the command \n\tto exit enter $$\n'
	print(intro2)
	while operation != "$$":
		operation = input("\n\t? ")
	
		array, pointer, loop_pointer = operations_on_array(operation, array, pointer, loop_pointer)
"""
# begin_x = 20 ; begin_y = 7
# height = 5 ; width = 40
# win = curses.newwin(height, width, begin_y, begin_x)


def interface():
	memory = Memory()
	mode = 'c'
	screen = curses.initscr()
	curses.echo()
	reg = True

	while True:
		screen.clear()
		if mode == 'c':
			cmd_view(screen)
			memory_map(screen)
		
		screen.addstr(17, 1, '	? ' )	
		screen.addstr(19, 1, "	________________________________________")
		user_input = screen.getstr(17, 10, 3).decode('utf-8')
		
		operator, operand = 'a', '0'
		if ' ' in user_input:
			try:
				operator, operand = user_input.split(' ')
			except Error:
				return status
				screen.addstr(50, 1, "invalid string input")
		else:
			operator = user_input
		
		if operator == 'c':
			if mode == 'c':
				screen.addstr(50, 1, "already cmd mode")
			else:
				mode = 'c'
		 
		elif operator == 'm':
			if mode == 'm':
				screen.addstr(50, 1, "already memory map mode")
			else:
				mode = 'm'
		elif operator == 'q':
			curses.endwin()
			return 
		else:
			status = memory.handle_operations(operator, operand)
			# screen.addstr(50, 1, str(status.items()))
			# screen.addstr(51, 1, str(status.items()))	
		screen.refresh()
	curses.endwin()
