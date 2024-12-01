input = open("input").read().splitlines()

leftlist = []
rightlist = []

for lines in input:
    leftlist.append(lines[0:5])
    rightlist.append(lines[8:13])

sumlist = []
total = 0
for i, item in enumerate(leftlist):
    total += int(item) * int(rightlist.count(leftlist[i]))
print(total)
