from letter_finder import LetterFinder
 
# Part 1

filestream = open('data.txt', 'r') 
data = filestream.readlines()

io_combined_lines = []
lines = []
for line in data:
    line = line.replace('\n', '')
    io_combined_lines.append(line)
    line = line.split(' | ')
    line_input = line[0].split(' ')
    line_output = line[1].split(' ')
    data = { 'input': line_input, 'output': line_output }
    lines.append(data)

total_1s = 0
total_4s = 0
total_7s = 0
total_8s = 0

for line in lines:
    for num in line['output']:
        if len(num) == 2:
            total_1s += 1
        elif len(num) == 4:
            total_4s += 1
        elif len(num) == 3:
            total_7s += 1
        elif len(num) == 7:
            total_8s += 1    

combined_total = total_1s + total_4s + total_7s + total_8s
print(combined_total)


# Part 2

total_from_outputs = 0
for line in lines:
    letter_finder = LetterFinder(line['input'])
    letter_finder.find_letters()
    letter_finder.convert_output(line['output'])
    total_from_outputs += letter_finder.convert_output(line['output'])

print(total_from_outputs)