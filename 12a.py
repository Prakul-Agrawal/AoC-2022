tempgrid = []
grid = []
while True:
    s = input()
    if s == '-1':
        break
    else:
        grid.append(s)
        if 'S' in s:
            s = s.replace('S','a')
        if 'E' in s:
            s = s.replace('E','z')
        tempgrid.append(s)

n = len(grid)
m = len(grid[0])

adj = [[] for i in range(n*m)]

for i in range(n):
    for j in range(m):
        if j+1 < m:
            x = tempgrid[i][j]
            y = tempgrid[i][j+1]
            if ord(x) >= ord(y) - 1:
                adj[m*i + j].append(m*i + j + 1)
        if j-1 > -1:
            x = tempgrid[i][j]
            y = tempgrid[i][j-1]
            if ord(x) >= ord(y) - 1:
                adj[m*i + j].append(m*i + j - 1)
        if i+1 < n:
            x = tempgrid[i][j]
            y = tempgrid[i+1][j]
            if ord(x) >= ord(y) - 1:
                adj[m*i + j].append(m*i + j + m)
        if i-1 > -1:
            x = tempgrid[i][j]
            y = tempgrid[i-1][j]
            if ord(x) >= ord(y) - 1:
                adj[m*i + j].append(m*i + j - m)

Spos = 0
Epos = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            Spos = m*i + j
        elif grid[i][j] == 'E':
            Epos = m*i + j

array = [(Spos,0)]
visited = [0 for i in range(n*m)]
visited[0] = 1

while array != []:
    x,y = array.pop(0)
    for i in adj[x]:
        if visited[i] == 0:
            if i == Epos:
                print(y+1)
                break
            array.append((i,y+1))
            visited[i] = 1
    else:
        continue
    break
    
    
    



                
