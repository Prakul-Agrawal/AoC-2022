grid = [[0 for i in range(2000)] for j in range(2000)]

H = [1000,1000]
T = [1000,1000]
grid[1000][1000] = 1

while True:
    s = input().split()
    if s == ['-1']:
        break
    for i in range(int(s[1])):
        if s[0] == 'U':
            H[0] -= 1
        elif s[0] == 'D':
            H[0] += 1
        elif s[0] == 'R':
            H[1] += 1
        else:
            H[1] -= 1
            
        if abs(H[0] - T[0]) < 2 and abs(H[1] - T[1]) < 2:
            continue
        
        if s[0] == 'U':
            T[0] = H[0] + 1
            T[1] = H[1]
        elif s[0] == 'D':
            T[0] = H[0] - 1
            T[1] = H[1]
        elif s[0] == 'R':
            T[1] = H[1] - 1
            T[0] = H[0]
        else:
            T[1] = H[1] + 1
            T[0] = H[0]

        grid[T[0]][T[1]] = 1

count = 0
for i in grid:
    for j in i:
        if j == 1:
            count += 1

print(count)
        

