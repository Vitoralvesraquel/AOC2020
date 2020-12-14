--- Day 8: Handheld Halting ---

A boot code is executing a infinite loop. The boot code is represented as a
text file (input.txt) with one instruction per line of text.

Each instruction consists of an operation (acc, jmp, or nop) and an argument
(a signed number like +4 or -20).

acc: increases or decreases a single global value called the accumulator by
the value given in the argument. The accumulator starts at 0. After an acc instruction, the instruction
immediately below it is executed next.

jmp: jumps to a new instruction relative to itself. The next instruction to
execute is found using the argument as an offset from the jmp instruction.

nop: stands for No Operation - it does nothing. The instruction immediately below it is executed next.

    Part 1: Run your copy of the boot code. Immediately before any instruction is executed a second time,
    what value is in the accumulator?

    Part 2: Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
    What is the value of the accumulator after the program terminates?

source: https://adventofcode.com/2020/day/8