# https://adventofcode.com/2021/day/3

import sys

# read input
with open("./input3.txt") as f:
    inputs = f.readlines()
inputs = [x.replace("\n", "") for x in inputs]
print(inputs)
print(len(inputs))

count_ones = [0] * len(inputs[0])
for i in inputs:
    for j in range(len(i)):
        if i[j] == "1":
            count_ones[j] += 1
print(count_ones)

first_number = 0
first_binary = ""
second_number = 0
second_binary = ""

for i in range(len(count_ones)):
    # print(count_ones[i], (len(inputs) / 2), len(count_ones) - i - 1)
    if count_ones[i] > (len(inputs) / 2):
        first_number += 2**(len(count_ones) - i - 1)
        first_binary = first_binary + "1"
        second_binary = second_binary + "0"
    else:
        second_number += 2**(len(count_ones) - i - 1)
        first_binary = first_binary + "0"
        second_binary = second_binary + "1"
    # print(first_binary, second_binary, first_number, second_number)

print(first_number, second_number, first_number * second_number)
print(first_binary, second_binary)

# Part 2
# Oxygen generator rating
oxygen_inputs = inputs[:]

oxygen_rating = ""
iteration = 0
while len(oxygen_inputs) > 1:
    count_ones = 0
    for oxygen_input in oxygen_inputs:
        if oxygen_input[iteration] == "1":
            count_ones += 1
    keep = "1"
    if count_ones >= (len(oxygen_inputs) / 2):
        keep = "1"
    else:
        keep = "0"
    oxygen_inputs = [x for x in oxygen_inputs if x[iteration] == keep]
    iteration += 1

# CO2 scrubber rating
co2_inputs = inputs[:]

oxygen_rating = ""
iteration = 0
while len(co2_inputs) > 1:
    count_ones = 0
    for co2_input in co2_inputs:
        if co2_input[iteration] == "1":
            count_ones += 1
    keep = "1"
    if count_ones >= (len(co2_inputs) / 2):
        keep = "0"
    else:
        keep = "1"
    co2_inputs = [x for x in co2_inputs if x[iteration] == keep]
    iteration += 1

print(oxygen_inputs, co2_inputs)
print(int(oxygen_inputs[0], 2), int(co2_inputs[0], 2), int(oxygen_inputs[0], 2) * int(co2_inputs[0], 2))
