grid = [[0 for x in range(1001)] for y in range(200)]
maxy = 0
while True:
    s = input().split()
    if s == ['-1']:
        break
    length = len(s)
    for i in range(0,length-2,2):
        a,b = list(map(int,s[i].split(',')))
        c,d = list(map(int,s[i+2].split(',')))
        if max(b,d) > maxy:
            maxy = max(b,d)
        if a == c:
            for j in range(min(b,d),max(b,d)+1):
                grid[j][a] = 1
        else:
            for j in range(min(a,c),max(a,c)+1):
                grid[b][j] = 1

for i in range(1001):
    grid[maxy+2][i] = 1

count = 0
flag = 0
while True:
    pos = [0,500]
    while True:
        if grid[pos[0]+1][pos[1]] == 0:
            pos[0] += 1
        elif grid[pos[0]+1][pos[1]-1] == 0:
            pos[0] += 1
            pos[1] -= 1
        elif grid[pos[0]+1][pos[1]+1] == 0:
            pos[0] += 1
            pos[1] += 1
        else:
            grid[pos[0]][pos[1]] = 1
            count += 1
            if pos[0] == 0 and pos[1] == 500:
                flag = 1
            break
    if flag == 1:
        break

print(count)
        

        
    
