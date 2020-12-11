# Part 1
field_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with open('passport_batch.txt') as batch:
    passport_line = ''
    valid = 0
    for line in batch:
        if line == '\n':
            if all(fields in passport_line for fields in field_list):
                valid = valid + 1
            passport_line = ''
            continue
        passport_line = passport_line + line
    if all(fields in passport_line for fields in field_list):
        valid = valid + 1
print('Valid passports:',valid)

# Part 2
def passport_check(passport):
    """
    :type passport: str
    """
    import string
    field_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    counter = 0
    for field in field_list:
        field_pos = passport.find(field)
        if field_pos != -1:
            field_input = passport[field_pos + 4:passport.find(' ', field_pos)]
            if field == 'byr' and len(field_input) == 4 and 1920 <= int(field_input) <= 2002:
                counter += 1
            elif field == 'iyr' and len(field_input) == 4 and 2010 <= int(field_input) <= 2020:
                counter += 1
            elif field == 'eyr' and len(field_input) == 4 and 2020 <= int(field_input) <= 2030:
                counter += 1
            elif field == 'hgt':
                if field_input[-2:] == 'cm' and 150 <= float(field_input[:-2]) <= 193:
                    counter += 1
                if field_input[-2:] == 'in' and 59 <= float(field_input[:-2]) <= 76:
                    counter += 1
            elif field == 'hcl' and field_input[0] == '#' and all(
                    digit in string.hexdigits for digit in field_input[1:]):
                counter += 1
            elif field == 'ecl' and field_input in 'amb blu brn gry grn hzl oth'.split():
                counter += 1
            elif field == 'pid' and len(field_input) == 9:
                try:
                    int(field_input)
                    counter += 1
                except:
                    break
    if counter == 7:
        return 1


with open('passport_batch.txt') as batch:
    passport_line = ''
    valid = 0
    for line in batch:
        if line == '\n':
            if passport_check(passport_line) == 1:
                valid += 1
            passport_line = ''
            continue
        new_line = line.replace('\n', ' ')
        passport_line += new_line
    if passport_check(passport_line) == 1:
        valid += 1
print('Valid passports part II:', valid)
