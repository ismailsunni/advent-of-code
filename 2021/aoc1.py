# https://adventofcode.com/2021/day/1

import sys

# read input
with open('./input1.txt') as f:
    inputs =  f.readlines()
inputs = [int(x.replace('\n', '')) for x in inputs]
print(inputs)

# Part 1
num_increasing = 0
for i in range(len(inputs) - 1):
    if inputs[i + 1] > inputs[i]:
        num_increasing += 1

print(num_increasing)

# Part 2
num_increasing = 0
for i in range(len(inputs) - 3):
    if inputs[i + 3] > inputs[i]:
        num_increasing += 1

print(num_increasing)
