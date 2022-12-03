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