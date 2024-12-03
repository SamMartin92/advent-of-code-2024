f = open("input.txt", "r")

codes = [line.split() for line in f]

sol=0


for code in codes:
    is_increasing = all(int(i) < int(j) for i, j in zip(code, code[1:]))
    is_decreasing = all(int(i) > int(j) for i, j in zip(code, code[1:]))
    safe = all(abs(int(i)-int(j))<=3 for i,j in zip(code, code[1:]))
    if is_decreasing or is_increasing:
        if safe:
            sol+=1
              
print(sol)

