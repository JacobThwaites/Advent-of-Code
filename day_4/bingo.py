from formatter import Formatter

filestream = open('data.txt', 'r') 

data = filestream.readlines()
formatter = Formatter()
numbers_called = formatter.get_numbers_called(data)
bingo_cards = formatter.get_bingo_cards(data)

def mark_number(num_called, card):
    for row in card:
        for i in range(len(row)):
            if row[i] == num_called:
                row[i] = 'called'

def is_card_winner(card):
    if has_complete_row(card) or has_complete_column(card):
        return True
    return False

def has_complete_row(card):
    for row in card:
        if is_row_winner(row):
            return True
    return False

def is_row_winner(row):
    for num in row:
        if num != 'called':
            return False 
    return True
    

def has_complete_column(card):
    for i in range(len(card[0])):
        if is_column_winner(card, i):
            return True
    return False  

def is_column_winner(card, index):
    for row in card:
        if row[index] != 'called':
            return False 
    return True 

def calculate_sum_unmarked_nums(card):
    sum_unmarked_nums = 0
    for row in card:
        for num in row:
            if num != 'called':
                sum_unmarked_nums += num
    return sum_unmarked_nums

def find_winner():
    for num in numbers_called:
        for card in bingo_cards:
            mark_number(num, card)
            if is_card_winner(card):
                sum_unmarked_nums = calculate_sum_unmarked_nums(card)
                return num * sum_unmarked_nums

def find_loser(bingo_cards):
    for num in numbers_called:
        for card in list(bingo_cards):
            mark_number(num, card)
            if is_card_winner(card):
                if len(bingo_cards) != 1:
                    bingo_cards.remove(card)
                else: 
                    return calculate_sum_unmarked_nums(bingo_cards[0]) * num


# print('winner:')
# print(find_winner())
# print('loser:')
print(find_loser(bingo_cards))