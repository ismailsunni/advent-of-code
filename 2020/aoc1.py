import sys

# read input
with open("./input1.txt") as f:
    inputs = f.readlines()
inputs = [int(x.replace("\n", "")) for x in inputs]
print(inputs)

# aoc day 1 question 1
found = False
for i in range(len(inputs)):
    for j in range(i + 1, len(inputs)):
        if inputs[i] + inputs[j] == 2020:
            print(inputs[i], inputs[j], inputs[i] * inputs[j])
            found = True
            break
    if found:
        break

# aoc day 1 question 2
found = False
for i in range(len(inputs)):
    for j in range(i + 1, len(inputs)):
        for k in range(j + 1, len(inputs)):
            if inputs[i] + inputs[j] + inputs[k] == 2020:
                print(
                    inputs[i], inputs[j], inputs[k], inputs[i] * inputs[j] * inputs[k]
                )
                found = True
                break
        if found:
            break
    if found:
        break
