f = open("input.txt", "r")

l1, l2 = ([] for i in range(2))

for line in f:
    l1.append(int(line.split()[0]))
    l2.append(int(line.split()[1]))

l1.sort()
l2.sort()

sol=0

for i in range(len(l1)):
    sol+=abs(l1[i]-l2[i])

print(sol)
