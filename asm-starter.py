https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#!/usr/bin/python3

"""
CS-UY 2214
Jeff Epstein
Starter code for E20 assembler
asm.py
"""

import argparse

opcode = { "add":0, "sub":0, "or":0, "and":0, "slt":0, "jr":0,
            "slti":7, "lw":4, "sw":5, "jeq":6, "addi":1,
             "j":2, "jal":3, "movi":1, "nop":0, "halt":2  }

def print_machine_code(address, num):
    """
    print_line(address, num)
    Print a line of machine code in the required format.
    Parameters:
        address: int = RAM address of the instructions
        num: int = numeric value of machine instruction 

    For example: 
        >>> print_machine_code(3, 42)
        ram[3] = 16'b0000000000101010;    
    """
    instruction_in_binary = format(num,'016b')
    print("ram[%s] = 16'b%s;" % (address, instruction_in_binary))


def main():
    parser = argparse.ArgumentParser(description='Assemble E20 files into machine code')
    parser.add_argument('filename', help='The file containing assembly language, typically with .s suffix')
    cmdline = parser.parse_args()

    # our final output is a list of ints values representing
    # machine code instructions
    instructions=[]
    # iterate through the line in the file, construct a list
    # of numeric values representing machine code
    with open(cmdline.filename) as f:
        for line in f:
            line = line.split("#",1)[0].strip()    # remove comments
            instructions.append(len(line))
             # TODO change this. generate the machine code

    # print out each instruction in the required format
    for address, instruction in enumerate(instructions):
        print_machine_code(address, instruction) 


if __name__ == "__main__":
    main()

#ra0Eequ6ucie6Jei0koh6phishohm9