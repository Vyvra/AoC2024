input = open("input").read().splitlines()

leftlist = []
rightlist = []

for lines in input:
    leftlist.append(lines[0:5])
    rightlist.append(lines[8:13])

leftlist.sort()
rightlist.sort()

sumlist = []

for i, line in enumerate(leftlist):
    sumlist.append(abs(int(leftlist[i]) - int(rightlist[i])))

print(sum(sumlist))
