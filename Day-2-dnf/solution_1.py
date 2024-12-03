f = open("input.txt", "r")

codes = [line.split() for line in f]

# codes = [[7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9]]
sol=len(codes)


# res = all(i < j for i, j in zip(test_list, test_list[1:]))

for code in codes:
    is_increasing = all(i < j for i, j in zip(code, code[1:]))
    is_decreasing = all(i > j for i, j in zip(code, code[1:]))
    # print (is_increasing)
    # print (is_decreasing)
    # if not is_decreasing:
    #     sol-=1
    # else:
    for level in range(len(code)-1):
        # if code[level] == code[level +1]:
        #     sol-=1
        print(f"First:{int(code[level])} Second: {int(code[level+1])} Result:{abs(int(code[level]) - int(code[level+1]) )}" + f" {abs(int(code[level]) - int(code[level+1]) )>3}")
        if abs(int(code[level]) - int(code[level+1]) )>3:
            sol-=1
            break

    
        

      
        
            
print(sol)

