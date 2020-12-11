# Part I - maximum and minimum times a letter can appear

with open('input_file.txt') as input_file:
    valid = 0
    invalid = 0
    for line in input_file:
        letter_min = int(line[0:line.index('-')])
        letter_max = int(line[line.index('-') + 1:line.index(' ')])
        letter = line[line.index(':') - 1]

        if line.count(letter) - 1 < letter_min or line.count(letter) - 1 > letter_max:
            invalid = invalid + 1
        else:
            valid = valid + 1

print('Part I')
print('Valid passwords:', valid)
print('Invalid passwords:', invalid)

# Part II - Exactly one of the positions must contain letter

with open('input_file.txt') as input_file:
    new_valid = 0
    new_invalid = 0
    for line in input_file:
        position_1 = int(line[0:line.index('-')])
        position_2 = int(line[line.index('-') + 1:line.index(' ')])
        letter = line[line.index(':') - 1]
        password = line[line.index(':') + 2:]
        if password[position_1 - 1] == letter and password[position_2 - 1] == letter:
            new_invalid = new_invalid + 1
        elif password[position_1 - 1] != letter and password[position_2 - 1] != letter:
            new_invalid = new_invalid + 1
        else:
            new_valid = new_valid + 1


print('Part II')
print('Valid passwords:', new_valid)
print('Invalid passwords:', new_invalid)
