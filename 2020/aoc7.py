# read input
with open("./input7.txt") as f:
    lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]


def parse_rule(line):
    # remove the bags, bag, and '.'
    line = line.replace(" bags", "").replace(" bag", "").replace(".", "")
    # split between outer bag and inner bags
    outer_bag, inner_bags = line.split(" contain ")
    # split the inner bags
    inner_bags = inner_bags.split(", ")
    # get the number and the color. The number is always 1 digit
    try:
        inner_bags = [(int(ib[0]), ib[2:]) for ib in inner_bags]
    except ValueError:
        inner_bags = []
    # print(outer_bag, inner_bags)
    # make proper dict
    return {outer_bag: {ib[1]: ib[0] for ib in inner_bags}}


all_rules = {}
for line in lines:
    dict_rule = parse_rule(line)
    all_rules = {**all_rules, **dict_rule}

print(all_rules)


def has_shinny_gold(bag_color):
    rule = all_rules[bag_color]
    if "shiny gold" in rule.keys():
        return True
    else:
        for inner_bag_color in rule.keys():
            if has_shinny_gold(inner_bag_color):
                return True
    return False


contain_shinny_gold = [has_shinny_gold(bag) for bag in all_rules.keys()]
print(len(contain_shinny_gold))
print(contain_shinny_gold.count(True))

# question 2
def count_bag(bag_color):
    if len(all_rules[bag_color]) == 0:
        return 0
    else:
        inside_bag = 0
        for color, number in all_rules[bag_color].items():
            inside_bag += number + number * count_bag(color)
        return inside_bag


print(count_bag("shiny gold"))
