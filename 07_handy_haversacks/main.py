import re

with open('input.txt', 'r') as rules_file:
    file_len = 0
    for line in rules_file:
        file_len += 1
my_bag = '1 shiny gold'
containers_list = [my_bag]
contents_list = [my_bag]
bag_count = 0
i = 0
while i < 2 * file_len:
    with open('input.txt', 'r') as rules_file:
        for line in rules_file:
            i += 1

            container = line[:line.index(' bag')]
            content = line[line.index('contain') + 8:]
            for out_bag in containers_list:
                if out_bag[re.search('\D', out_bag).start():] in content and container not in containers_list:
                    containers_list.append(container)
                    i = 0

            content = content.replace(', ', ',').strip('.\n ').split(',')
            for in_bag in contents_list:
                in_bag_colour = in_bag[in_bag.index(' ')+1:]
                in_bag_number = int(in_bag[0:in_bag.index(' ')])
                if in_bag_colour in container:
                    for sub_bag in content:
                        if sub_bag[0] != 'n':
                            sub_bag_number = int(sub_bag[0:sub_bag.index(' ')]) * in_bag_number
                            sub_bag_colour = sub_bag[sub_bag.index(' '):sub_bag.index(' bag')]
                            bag_count += sub_bag_number
                            contents_list.append(str(sub_bag_number) + sub_bag_colour)
                            i = 0
                    contents_list.remove(in_bag)

print('Bags that can contain my_bag:', len(containers_list) - 1)  # Part 1
print('Bags required inside my_bag:', bag_count)  # Part 2
