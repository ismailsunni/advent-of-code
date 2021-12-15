# read input
with open('./input6.txt') as f:
    text =  f.read()

groups = text.split('\n\n')

# question 1
group_answers = [group.replace('\n', '') for group in groups]
print(group_answers)
# concat all the answer in the group (also remove the \n), convert to set then count the number of element
yes_answers = [len(set(group_answer)) for group_answer in group_answers]
print(sum(yes_answers))

# question 2
group_answers = [group.split('\n') for group in groups]
print(group_answers)
# convert the group answer to set, the do intersect among them  (* char is used to convert list to args parameter)
# then count the element on that set group
all_yes_questions = [len(set.intersection(*[set(ga) for ga in group_answer])) for group_answer in group_answers]
print(sum(all_yes_questions))
