filestream = open('data.txt', 'r') 
data = filestream.readlines()

opening_brackets = {
        '(': ')',
        '<': '>',
        '{': '}',
        '[': ']'
    }

closing_brackets = {
    ')': '(',
    '>': '<',
    '}': '{',
    ']': '['
}

illegal_bracket_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

fixing_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

total_score = 0

incomplete_line_fixes = []

for line in data:
    is_line_corrupted = False
    line = line.replace('\n', '')
    opening_bracket_queue = []
    for b in line:
        if b in opening_brackets:
            opening_bracket_queue.append(b)
        elif closing_brackets[b] == opening_bracket_queue[-1]:
            opening_bracket_queue.pop()
        else: 
            total_score += illegal_bracket_scores[b]
            opening_bracket_queue = []
            is_line_corrupted = True
            break

    if is_line_corrupted:
        is_line_corrupted = False
        continue 
    else:
        score = 0
        while len(opening_bracket_queue) > 0:
            score *= 5
            score += fixing_scores[opening_bracket_queue.pop()]

        incomplete_line_fixes.append(score)

incomplete_line_fixes.sort()
mid = int((len(incomplete_line_fixes) -1) / 2)

print(incomplete_line_fixes[mid])