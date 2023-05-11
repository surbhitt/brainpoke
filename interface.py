import curses
import brainpoke 

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
	memory = brainpoke.Memory()
	mode = ord('c')
	screen = curses.initscr()
	curses.echo()
	reg = True

	while True:
		screen.clear()
		if mode == ord('c'):
			cmd_view(screen)
		elif mode == ord('m'):
			memory_map(screen)
		
		screen.addstr(20, 1, '	? ' )	
		user_input = screen.getch()
		screen.getch()
		if user_input == ord('c'):
			if mode == ord('c'):
				screen.addstr(50, 1, "already cmd mode")
			else:
				mode = ord('ord')
		 
		elif user_input == ord('m'):
			if mode == ord('m'):
				screen.addstr(50, 1, "already memory map mode")
			else:
				mode = ord('m')
		elif user_input == ord('q'):
			curses.endwin()
			return 0
		else:
			memory.handle_operations(user_input)
	
		screen.refresh()
	curses.endwin()
