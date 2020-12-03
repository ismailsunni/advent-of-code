from functools import reduce
# read input
with open('./input3.txt') as f:
    lines =  f.readlines()
lines = [line.replace('\n', '') for line in lines]
print(lines)
num_of_lines = len(lines)
line_length = len(lines[0])
print(num_of_lines)
print(line_length)

def tree_counter(i_increment, j_increment):
    i = 0
    j = 0
    encounters = []
    while i < num_of_lines:
        # print(i, lines[i])
        normalized_j = j % len(lines[i])
        encounters.append(lines[i][normalized_j])
        i += i_increment
        j += j_increment
    return encounters.count('#')

print(tree_counter(1, 3))
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
num_trees = []
for slope in slopes:
    num_tree = tree_counter(slope[0], slope[1])
    num_trees.append(num_tree)
print(num_trees)
result_part_2 = reduce((lambda x, y: x * y), num_trees)
print(result_part_2)