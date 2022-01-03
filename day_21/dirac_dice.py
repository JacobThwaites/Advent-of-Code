# Player 1 starting position: 7
# Player 2 starting position: 1

p1 = 7
p2 = 1
p1_score = p2_score = 0
is_p1_turn = True
d = 6
num_rolls = 0
while p1_score < 1000 and p2_score < 1000:
    if is_p1_turn:
        p1 = (p1 + d) % 10 if (p1 + d) % 10 != 0 else 10
        p1_score += p1
    else:
        p2 = (p2 + d) % 10 if (p2 + d) % 10 != 0 else 10
        p2_score += p2
    d += 9
    is_p1_turn = not is_p1_turn
    num_rolls += 3

print(p1_score)
print(p2_score)
print(min(p1_score, p2_score) * num_rolls)