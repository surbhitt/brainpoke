
#!/usr/bin/env python3

"""to do"""






def viewstate (array):
    print(array)
def menu ():
    Intro_prompt = """
    Th1s i$ hte brainFook program
    implement@tion of the brainf**k in python
    ______
    """
    print(Intro_prompt)



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




def main ():
    menu ()
    # the master memory
    array = [0] * 30000
    pointer = 0
    loop_pointer = [-1, -1]

    operation = 0 
    intro2 = "\ton ? prompt enter the command \n\tto exit enter $$\n"
    print(intro2)
    while operation != "$$":
        operation = input("\n\t? ")
        array, pointer, loop_pointer = operations_on_array(operation, array, pointer, loop_pointer)

if __name__ == '__main__':
    main()