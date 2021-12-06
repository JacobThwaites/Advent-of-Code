data = open('data.txt', 'r') 
binary = data.readLines()

occurrences = {}
for i in range(len(binary[0]) - 1):
    occurrences[i] = {0:0, 1:0}

for num in binary: 
    for i in range(len(num) - 1):
        digit = int(num[i])
        occurrences[i][digit] += 1

gamma_rate = ''
epsilon_rate = ''

for i in range(len(binary[0] - 1)):
    if occurrences[i][0] > occurrences[i][1]:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

result = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(result)