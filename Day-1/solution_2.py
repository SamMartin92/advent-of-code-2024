f = open("input.txt", "r")

l1, l2 = ([] for i in range(2))

for line in f:
    l1.append(int(line.split()[0]))
    l2.append(int(line.split()[1]))

sol=0
sim_scores = {}

for i in range(len(l1)):
    sim_scores[l1[i]] = l2.count(l1[i])*l1[i]

    
print(sum(sim_scores.values()))