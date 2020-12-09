# read input
with open('./input9.txt') as f:
    lines =  f.readlines()
lines = [line.replace('\n', '') for line in lines]
numbers = [int(n) for n in lines]

print(numbers)
print(len(numbers))

# question 1
def has_sum(possible_numbers, target):
    for first_number in possible_numbers:
        second_number = target - first_number
        if second_number in possible_numbers:
            return True
        # not so efficient here, since it will check for all possible number
    else:
        return False

for i in range(25, len(numbers)):
    if not has_sum(numbers[i - 25:i], numbers[i]):
        break
print(i)
invalid_number = numbers[i]
print('invalid number', invalid_number)

# question 2
found = False
for i in range(len(numbers)):
    if found:
        break
    for j in range(i, len(numbers)):
        if sum(numbers[i:j]) == invalid_number:
            print(i, j)
            print(numbers[i:j], sum(numbers[i:j]))
            # min, max, and min + max
            print(min(numbers[i:j]), max(numbers[i:j]), min(numbers[i:j]) + max(numbers[i:j]))
            found = True
            break
