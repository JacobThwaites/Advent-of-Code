def max_index(arr):
    index = 0
    mx = float('-inf')

    for i, v in enumerate(arr):
        if v > mx:
            mx = v
            index = i
    
    return index

def min_index(arr):
    index = 0
    mn = float('inf')

    for i, v in enumerate(arr):
        if v < mn:
            mn = v
            index = i
    
    return index


class Trie:
    def __init__(self):
        self.chars = {}
    
    def add_word(self, word: str):
        temp = self.chars

        for char in word:
            if char not in temp: 
                temp[char] = {}
            temp = temp[char]
        
        temp['end of word'] = True

    def contains_word(self, word: str) -> bool:
        temp = self.chars 

        for char in word:
            if char not in temp:
                return False 
            temp = temp[char]
        
        return 'end of word' in temp

    def contains_prefix(self, word: str) -> bool:
        temp = self.chars 

        for char in word: 
            if char not in temp:
                return False 
            temp = temp[char] 
        
        return True 