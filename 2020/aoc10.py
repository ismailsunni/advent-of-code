# read input
with open('./input10.txt') as f:
    lines =  f.readlines()
lines = [line.replace('\n', '') for line in lines]
jolts = [int(n) for n in lines]

sorted_jolts = sorted(jolts)

print(sorted_jolts)
print(len(sorted_jolts))
# Add the device's built in joltage
full_sorted_jolts = [0] + sorted_jolts + [max(sorted_jolts) + 3]

# question 1
num_diff_1 = 0
num_diff_3 = 0
for i in range(len(full_sorted_jolts) - 1):
    if full_sorted_jolts[i + 1] - full_sorted_jolts[i] == 1:
        num_diff_1 += 1
    elif full_sorted_jolts[i + 1] - full_sorted_jolts[i] == 3:
        num_diff_3 += 1

print(num_diff_1, num_diff_3, num_diff_1 * num_diff_3)

# question 2
# 0
# 1 2
# 2