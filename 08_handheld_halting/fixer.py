# Part 1:
with open('input.txt') as input_file:
    line_list = []
    line_number = 0
    for line in input_file:
        line_number += 1
        line_list.append(str(line_number) + ',' + line)

accumulator = 0
line_number_list = []
next_line = 1
loop_exit = 0
while loop_exit == 0:
    for line_a in line_list:
        line_index = int(line_a[0:line_a.index(',')])
        rule = line_a[line_a.index(',') + 1:line_a.index(' ')]
        argument = int(line_a[line_a.index(' ') + 1:line_a.index('\n')])
        if line_index == next_line:
            if line_index in line_number_list:
                loop_exit = 1
                break

            line_number_list.append(line_index)
            if rule == 'acc':
                accumulator += argument
                next_line += 1
            elif rule == 'jmp':
                next_line += argument
            else:
                next_line += 1

print('Accumulator before fixing:', accumulator)

# Part 2:
with open('input.txt') as input_file:
    line_list = []
    line_number = 0
    for line in input_file:
        line_number += 1
        line_list.append(str(line_number) + ',' + line)

accumulator_fix = 0
line_number_list = []
next_line = 1
loop_exit = 0
change_count = 1
jmp_nop_count = 0
last_line = len(line_list)
while loop_exit == 0:
    for line_a in line_list:
        line_index = int(line_a[0:line_a.index(',')])
        rule = line_a[line_a.index(',') + 1:line_a.index(' ')]
        argument = int(line_a[line_a.index(' ') + 1:line_a.index('\n')])
        if line_index == next_line:
            if line_index in line_number_list:
                accumulator_fix = 0
                line_number_list = []
                next_line = 1
                change_count += 1
                jmp_nop_count = 0
                break

            line_number_list.append(line_index)
            if rule == 'acc':
                accumulator_fix += argument
                next_line += 1
            elif rule == 'jmp':
                jmp_nop_count += 1
                if change_count == jmp_nop_count:
                    next_line += 1
                else:
                    next_line += argument
            else:
                jmp_nop_count += 1
                if change_count == jmp_nop_count:
                    next_line += argument
                else:
                    next_line += 1
        if next_line > last_line:
            loop_exit = 1
            break

print('Accumulator after fixing:', accumulator_fix)
