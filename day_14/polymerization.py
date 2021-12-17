from collections import Counter
import math

filestream = open('data.txt', 'r') 
data = filestream.readlines()

template = ''
steps = []


template = data[0].replace('\n', '')
template2 = template

for i in range(2, len(data)):
    data[i] = data[i].replace('\n', '')
    s = data[i].split(' -> ')
    step = {'pair': s[0], 'letter': s[1]}
    steps.append(step)
    steps.append(step)

def get_insertions_for_step(template, step):
    insertions = []
    i = 0
    j = 1
    while j < len(template):
        if template[i] == step['pair'][0] and template[j] == step['pair'][1]:
            insertions.append((j, step['letter']))
        i += 1
        j += 1
    return insertions

def get_insertions(template, steps):
    insertions = []
    for s in steps:
        insertions += get_insertions_for_step(template, s)
    insertions = set(insertions)
    return sorted(insertions)

def increment_letter_count(letter_count, letter):
    if letter not in letter_count:
        letter_count[letter] = 1
    else:
        letter_count[letter] += 1


# get starting letter count
letter_count = {}
for letter in template:
    increment_letter_count(letter_count, letter)

# convert template to array
template = list(template)

def perform_insertions(insertions):
    total_insertions = 0
    for insertion in insertions:
        index = insertion[0] + total_insertions
        template.insert(index, insertion[1])
        total_insertions += 1
        increment_letter_count(letter_count, insertion[1])



for i in range(10):
    insertions = get_insertions(template, steps)
    perform_insertions(insertions)


min_letter = math.inf
max_letter = 0
for v in letter_count.values():
    min_letter = min(v, min_letter)
    max_letter = max(v, max_letter)

# print(max_letter - min_letter)

# Part 2 
pair_counts = Counter()
for i in range(0, len(template2) - 1):
    pair_counts[template2[i: i + 2]] += 1

patterns = {}
for i in range(2, len(data)):
    src, dst = data[i].split(' -> ')
    patterns[src] = dst

for _ in range(40):
    new_pairs = Counter()
    char_counts = Counter()

    for k, v in pair_counts.items():
        new_pairs[f'{k[0]}{patterns[k]}'] += v
        new_pairs[f'{patterns[k]}{k[1]}'] += v

        char_counts[k[0]] += v
        char_counts[patterns[k]] += v
    
    pair_counts = new_pairs

char_counts[template2[-1]] += 1

counts = sorted(char_counts.values())

result = counts[-1] - counts[0]

print(result)