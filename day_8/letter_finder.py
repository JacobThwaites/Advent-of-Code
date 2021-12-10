class LetterFinder():
    def __init__(self, words):
        self.letters = {}
        self.conversion_letters = {}
        self.words = words

    def convert_output(self, output):
        conversion = ''
        for word in output:
            conversion = conversion + self.convert_word_to_num(word)
        
        return int(conversion)

    def convert_word_to_num(self, word):
        numbers_from_lit = {
            'abcefg': '0',
            'cf': '1',
            'acdeg': '2',
            'acdfg': '3', 
            'bcdf': '4',
            'abdfg': '5',
            'abdefg': '6',
            'acf': '7',
            'abcdefg': '8',
            'abcdfg': '9'
        }
        corrected = self.correct_letters_in_word(word)
        return numbers_from_lit[corrected]

    def correct_letters_in_word(self, word):
        converted = ''
        for letter in word:
            converted = converted + self.conversion_letters[letter]
        return self.sort_string(converted)

    def sort_string(self, str):
        return ''.join(sorted(str))

    def find_letters(self):
        self.find_letter_a()
        self.find_letter_c_and_f()
        self.find_letter_d()
        self.find_letter_b()
        self.find_letter_e()
        self.find_letter_g()
        self.set_conversion_letters()

    def find_letter_a(self):
        three_letter_word = self.find_word_by_length(3)
        two_letter_word = self.find_word_by_length(2)
        for letter in three_letter_word:
            if letter not in two_letter_word:
                self.letters['a'] = letter
        
    def find_word_by_length(self, length):
        for word in self.words:
            if len(word) == length:
                return word

        return False 

    def find_letter_c_and_f(self):
        two_letter_word = self.find_word_by_length(2)
        six_letter_words = self.find_multiple_words_by_length(6)
        letter_occurences = self.count_letter_occurrences(six_letter_words)
        for letter in two_letter_word:
            if letter_occurences[letter] == 2:
                self.letters['c'] = letter
            else:
                self.letters['f'] = letter

    def find_letter_d(self):
        six_letter_words = self.find_multiple_words_by_length(6)
        letter_occurences = self.count_letter_occurrences(six_letter_words)
        possible_letters = ['a', 'b', 'c', 'd', 'e','f','g']
        b_and_d = self.find_letter_b_or_d()
        for letter in possible_letters:
            if letter_occurences[letter] == 2 and letter != self.letters['c'] and letter in b_and_d:
                self.letters['d'] = letter 
                break

    def find_letter_b_or_d(self):
        four_letter_word = self.find_word_by_length(4)
        potential_letters = {}
        for letter in four_letter_word:
            if letter != self.letters['c'] and letter != self.letters['f']:
                potential_letters[letter] = True

        return potential_letters

    def find_multiple_words_by_length(self, length):
        words = []
        for word in self.words:
            if len(word) == length:
                words.append(word)
        return words

    def find_letter_b(self):
        four_letter_word = self.find_word_by_length(4)
        for letter in four_letter_word:
            if letter not in self.letters.values():
                self.letters['b'] = letter 
                break

    def find_letter_e(self):
        five_letter_words = self.find_multiple_words_by_length(5)
        letter_occurences = self.count_letter_occurrences(five_letter_words)
        for letter, count in letter_occurences.items():
            if letter != self.letters['b'] and count == 1:
                self.letters['e'] = letter
                break
    
    def count_letter_occurrences(self, words):
        letter_counts = {}
        for word in words:
            for letter in word:
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1
        return letter_counts

    def find_letter_c(self):
        six_letter_words = self.find_multiple_words_by_length(6)
        two_letter_word = self.find_word_by_length(2)
        letter_occurences = self.count_letter_occurrences(six_letter_words)
        for letter, count in letter_occurences.items():
            if count == 2 and letter != self.letters['b'] and letter != self.letters['d']:
                self.letters['c'] = letter
                break
    
    def find_letter_f(self):
        two_letter_word = self.find_word_by_length(2)
        for letter in two_letter_word:
            if letter != self.letters['c']:
                self.letters['f'] = letter
                break
    
    def find_letter_g(self):
        possible_letters = {'a': None,'b': None,'c': None,'d': None,'e': None,'f': None,'g': None}
        for key, val in self.letters.items():
            del possible_letters[val]
        
        for letter in possible_letters.keys():
            self.letters['g'] = letter
        
    
    def set_conversion_letters(self):
        for x, y in self.letters.items():
            self.conversion_letters[y] = x

# 2 digits - 1
# 3 digits - 7
# 4 digits - 4
# 5 digits - 2,3,5
# 6 digits - 0,6,9
# 7 digits - 8