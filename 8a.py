grid = []
while True:
    s = input()
    if s == '-1':
        break
    k = []
    for i in s:
        k.append(int(i))
    grid.append(k)

count = 0
n = len(grid)
m = len(grid[0])

newgrid = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    val = -1
    for j in range(m):
        if grid[i][j] > val:
            val = grid[i][j]
            newgrid[i][j] = 1

for i in range(n):
    val = -1
    for j in range(-1,-m-1,-1):
        if grid[i][j] > val:
            val = grid[i][j]
            newgrid[i][j] = 1

for j in range(m):
    val = -1
    for i in range(n):
        if grid[i][j] > val:
            val = grid[i][j]
            newgrid[i][j] = 1

for j in range(m):
    val = -1
    for i in range(-1,-n-1,-1):
        if grid[i][j] > val:
            val = grid[i][j]
            newgrid[i][j] = 1

for i in range(n):
    for j in range(m):
        count += newgrid[i][j]

print(count)
