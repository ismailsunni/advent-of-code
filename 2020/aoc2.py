# read input
with open('./input2.txt') as f:
    lines =  f.readlines()

# parse input
def parse_input(line):
    parts = line.split(':')
    password = parts[1].replace('\n', '').replace(' ', '')
    first_parts = parts[0].split(' ')
    letter = first_parts[1]
    first_number = int(first_parts[0].split('-')[0])
    second_number = int(first_parts[0].split('-')[1])
    return first_number, second_number, letter, password

def is_valid(line):
    min_occur, max_occur, letter, password = parse_input(line)
    if min_occur <= password.count(letter) <= max_occur:
        return True
    else:
        return False

def is_valid2(line):
    first_number, second_number, letter, password = parse_input(line)
    first_found = password[first_number - 1] == letter
    second_found = password[second_number - 1] == letter
    return first_found ^ second_found

print(lines)
valids = [is_valid(line) for line in lines]
print(valids.count(True))

valids = [is_valid2(line) for line in lines]
print(valids.count(True))
