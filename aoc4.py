import re

# read input
with open('./input4.txt') as f:
    text =  f.read()

lines = text.split('\n\n')
lines = [line.replace('\n', ' ') for line in lines]

# regex
hcl_pattern = re.compile(r"^#[0-9a-f]{6}$")
pid_pattern = re.compile(r"^[0-9]{9}$")

def parse(line):
    items = line.split(' ')
    items = {item.split(':')[0]: item.split(':')[1] for item in items}
    return items

def is_valid(item):
    mandatory_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    existing_keys = [key in item.keys() for key in mandatory_keys]
    return all(existing_keys)

def is_valid2(item):
    if not is_valid(item):
        return False

    if not (1920 <= int(item['byr']) <= 2002 and len(item['byr']) == 4):
        # print(int(item['byr']))
        return False

    if not (2010 <= int(item['iyr']) <= 2020 and len(item['iyr']) == 4):
        # print(int(item['iyr']))
        return False

    if not (2020 <= int(item['eyr']) <= 2030 and len(item['eyr']) == 4):
        # print(int(item['eyr']))
        return False

    try:
        height = int(item['hgt'][:-2])
        height_unit = item['hgt'][-2:]
        if height_unit == 'cm' and not (150 <= height <= 193):
            # print(item['hgt'])
            return False
        if height_unit == 'in' and not (59 <= height <= 76):
            # print(item['hgt'])
            return False
        if height_unit not in ['in', 'cm']:
            # print(item['hgt'])
            return False
    except ValueError as e:
        # no unit
        return False

    if not hcl_pattern.match(item['hcl']):
        # print(item['hcl'])
        return False

    if not item['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        # print(item['ecl'])
        return False

    if not pid_pattern.match(item['pid']):
        # print(item['pid'])
        return False

    return True

# part 1
is_valids = [is_valid(parse(line)) for line in lines]
# print(is_valids)
print(is_valids.count(True))

# part 2
is_valids2 = [is_valid2(parse(line)) for line in lines]
# print(is_valids2)
print(is_valids2.count(True))

# print(len(is_valids2))