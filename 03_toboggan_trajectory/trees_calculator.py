
with open('input_path.txt') as path_file:
    tree_multiplied = 1
    for path in path_file:
        stripped_path = path.strip()
        right_step = int(stripped_path[stripped_path.find(',') - 1])
        down_step = int(stripped_path[stripped_path.find('.') - 1])
        tree = 0
        position_right = 0
        line_count = 0
        with open('input_terrain.txt') as terrain_file:
            for line in terrain_file:
                stripped_line = line.strip()
                if line_count == 0 or line_count % down_step == 0:
                    if stripped_line[position_right] == '#':
                        tree = tree + 1
                    position_right = position_right + right_step
                if position_right >= len(stripped_line):
                    position_right = position_right - len(stripped_line)
                line_count = line_count + 1
        print(f'Trees in the path {stripped_path}: {tree}')
        tree_multiplied = tree_multiplied * tree
    print(f'Trees in each path multiplied: {tree_multiplied}')