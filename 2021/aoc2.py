# https://adventofcode.com/2021/day/2

import sys

# read input
with open("./input2.txt") as f:
    inputs = f.readlines()
inputs = [x.replace("\n", "").split(" ") for x in inputs]
print(inputs)

# Part 1
horizontal = 0
depth = 0
for i in inputs:
    movement = int(i[1])
    if i[0] == "forward":
        horizontal += movement
    elif i[0] == "down":
        depth += movement
    elif i[0] == "up":
        depth -= movement

print(horizontal, depth, horizontal * depth)

# Part 2
horizontal = 0
depth = 0
aim = 0
for i in inputs:
    movement = int(i[1])
    if i[0] == "forward":
        horizontal += movement
        depth += aim * movement
    elif i[0] == "down":
        aim += movement
    elif i[0] == "up":
        aim -= movement

print(horizontal, depth, horizontal * depth)
