class Formatter():
    def get_numbers_called(self, file_data):
        filestream = open('data.txt', 'r') 
        data = filestream.readlines()
        numbers_called = file_data[0]
        return self.create_numbers_called_array(numbers_called)

    def create_numbers_called_array(self, numbers_called):
        numbers_called = numbers_called.split(',')
        numbers_called[-1] = numbers_called[-1].strip('\n')
        for i in range(len(numbers_called)):
            numbers_called[i] = int(numbers_called[i])
        return numbers_called
    
    def get_bingo_cards(self, data):
        bingo_cards = self.create_bingo_cards_array(data)
        bingo_cards = self.format_rows(bingo_cards)
        return bingo_cards
        
    def create_bingo_cards_array(self, data):
        bingo_cards = []
        i = 2
        while i < len(data) - 1:
            card = []
            # remove empty space and new lines
            card.append(data[i].replace('  ',' ').split(' '))
            card[0][-1] = card[0][-1].strip('\n')
            card.append(data[i + 1].replace('  ',' ').split(' '))
            card[1][-1] = card[1][-1].strip('\n')
            card.append(data[i + 2].replace('  ',' ').split(' '))
            card[2][-1] = card[2][-1].strip('\n')
            card.append(data[i + 3].replace('  ',' ').split(' '))
            card[3][-1] = card[3][-1].strip('\n')
            card.append(data[i + 4].replace('  ',' ').split(' '))
            card[4][-1] = card[4][-1].strip('\n')
            bingo_cards.append(card)
            i += 6
        
        return bingo_cards
    
    def format_rows(self, bingo_cards):
        for card in bingo_cards:
            for row in card:
                if '' in row:
                    row.remove('')
                self.convert_strings_to_ints(row)
        return bingo_cards

    def convert_strings_to_ints(self, row):
        for i in range(len(row)):
            row[i] = int(row[i])