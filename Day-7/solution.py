f = open("test_input.txt", "r")

def collect_input(f):
    targets=[]
    inputs=[]

    for line in f:
        targets.append(int(line.split(": ")[0]))
        inputs.append(line.split(": ")[1].split())

    for input_list in inputs:
        for i in range(len(input_list)):
            input_list[i] = int(input_list[i])


    return targets, inputs

targets, inputs = collect_input(f)

combos=[]
for i in range(len(inputs)):
    combos.append(list(zip(inputs[i],inputs[i][1:])))


list_of_sums=[]
list_of_mults=[]
for i in range(len(combos)):
    sums=[]
    mults=[]
    for j in range(len(combos[i])):
        sums.append(sum(combos[i][j]))
        mults.append(combos[i][j][0]*combos[i][j][1])

    list_of_sums.append(sums)
    list_of_mults.append(mults)
    

print(list_of_sums[-1])
print(list_of_mults[-1])


results = []


for i in range(len(list_of_sums)):
    for j in range(len(list_of_mults)):
        results.append(list_of_sums[j])
        






