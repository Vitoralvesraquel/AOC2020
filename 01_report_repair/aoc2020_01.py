# Find the two entries that sum to 2020; what do you get if you multiply them together?
# what is the product of the three entries that sum to 2020?
with open('input_file.txt' ) as in_file:
    numbers_list = []
    for line in in_file:
        stripped_line = line.strip()
        numbers_list.append(int(stripped_line))

for number_1 in numbers_list:
    index_1 = numbers_list.index(number_1)
    index_2 = index_1 + 1
    while index_2 < len(numbers_list):
        number_2 = numbers_list[index_2]
        two_added = number_1 + number_2
        if two_added == 2020:
            two_multiplied = number_1 * number_2
            print(f'{number_1} + {number_2} = {two_added}')
            print(f'{number_1} * {number_2} = {two_multiplied}')

        index_3 = index_2 + 1
        while index_3 < len(numbers_list):
            number_3 = numbers_list[index_3]
            three_added = two_added + number_3
            if three_added == 2020:
                three_multiplied = number_1 * number_2 * number_3
                print(f'{number_1} + {number_2} + {number_3}= {three_added}')
                print(f'{number_1} * {number_2} * {number_3} = {three_multiplied}')
            index_3 = index_3 + 1
        index_2 = index_2 + 1
