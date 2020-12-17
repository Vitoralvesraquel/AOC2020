# Part I:
preamble = 25
before = []
count = 0
with open('input.txt') as input_file:
    for line in input_file:
        count += 1
        i = 0
        if count <= preamble:
            before.append(int(line))
            continue
        elif count > preamble:
            number = int(line)
            for n1 in before:
                n2 = number - n1
                if n2 in before[before.index(n1):] and n2 != n1:
                    before.append(number)
                    del before[0]
                    count = preamble
                    i = 1
                    break
        if i == 0:
            break
print('Part I: number =', number)

# Part II:
sum_set = []
with open('input.txt') as input_file:
    for line in input_file:
        sum_set.append(int(line))
        if number in sum_set:
            sum_set = []
        while sum(sum_set) > number:
            del sum_set[0]
        if sum(sum_set) == number:
            break
print('Part II: Smallest number + Largest number =', max(sum_set) + min(sum_set))
