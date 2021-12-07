filestream = open('data.txt', 'r') 
data = filestream.read()

fish = data.split(',')
for i in range(len(fish)):
    fish[i] = int(fish[i])

fish_count = []

for i in range(9):
    fish_count.append(0)


for f in fish:
    fish_count[f] += 1


# days_remaining = 80
# while days_remaining > 0:
#     new_fish = 0
#     for i in range(len(fish)):
#         if fish[i] == 0:
#             new_fish += 1
#             fish[i] = 6
#         else:
#             fish[i] -= 1
    
#     for n in range(new_fish):
#         fish.append(8)
    
#     days_remaining -= 1

# print(len(fish))


for i in range(256):
    fish_count.append(fish_count.pop(0))
    fish_count[6] += fish_count[8]

print(sum(fish_count))