import operator

data = open('data.txt', 'r') 
binary = data.readlines()

occurrences = {}
for i in range(len(binary[0]) - 1):
    occurrences[i] = {0:0, 1:0}

for num in binary: 
    for i in range(len(num) - 1):
        digit = int(num[i])
        occurrences[i][digit] += 1

oxygen = binary
co2 = []

def find_most_common(digit):
    if occurrences[digit][0] > occurrences[digit][1]:
        return 0
    else: return 1

digit = 0
i = 0
most_common = find_most_common(0)
while len(oxygen) > 1:
    print(oxygen[i][digit])
    if int(oxygen[i][digit]) != most_common:
        del oxygen[i]
    
    if i == len(oxygen) - 1:
        i = 0
        digit += 1
        most_common = find_most_common(digit)
    else: 
        i += 1

# for i in range(len(binary[0] - 1)):
#     if occurrences[i][0] > occurrences[i][1]:
#         gamma_rate += '0'
#         epsilon_rate += '1'
#     else:
#         gamma_rate += '1'
#         epsilon_rate += '0'

# result = int(gamma_rate, 2) * int(epsilon_rate, 2)
# print(oxygen)