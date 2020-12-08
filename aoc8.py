import copy
# read input
with open('./input8.txt') as f:
    lines =  f.readlines()
lines = [line.replace('\n', '') for line in lines]

instructions = [[line.split(' ')[0], int(line.split(' ')[1])] for line in lines]

print(instructions)
print(len(instructions))

def run(input):
    accumulator = 0
    current_instruction_index = 0
    already_run = []

    while current_instruction_index not in already_run and current_instruction_index < len(input):
        already_run.append(current_instruction_index)
        instruction = input[current_instruction_index]
        if instruction[0] == "nop":
            current_instruction_index += 1
        elif instruction[0] == "jmp":
            current_instruction_index += instruction[1]
        elif instruction[0] == "acc":
            current_instruction_index += 1
            accumulator += instruction[1]

    # return is_infinite, accumulator
    return not current_instruction_index not in already_run, accumulator

# question 1
print(run(instructions))

# question 2
is_infinite_loop = True
changed_index = 0
accumulator = 0

while is_infinite_loop and changed_index < len(instructions):
    # deep copy the list of instruction
    new_instructions = copy.deepcopy(instructions)
    if new_instructions[changed_index][0] == 'jmp':
        new_instructions[changed_index][0] = 'nop'
    elif new_instructions[changed_index][0] == 'nop':
        new_instructions[changed_index][0] = 'jmp'
    else:
        print(changed_index)
        changed_index += 1
        continue

    is_infinite_loop, accumulator = run(new_instructions)
    print(changed_index, is_infinite_loop, accumulator)
    changed_index += 1

print(accumulator)