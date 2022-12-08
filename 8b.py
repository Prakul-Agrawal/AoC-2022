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

newgrid = [[1 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or i == n - 1 or j == m - 1:
            newgrid[i][j] = 0
        else:
            x = grid[i][j]
            count = 0
            for k in range(j-1,-1,-1):
                if grid[i][k] < x:
                    count += 1
                else:
                    count += 1
                    break
            newgrid[i][j] *= count

            count = 0
            for k in range(j+1,m):
                if grid[i][k] < x:
                    count += 1
                else:
                    count += 1
                    break
            newgrid[i][j] *= count

            count = 0
            for k in range(i-1,-1,-1):
                if grid[k][j] < x:
                    count += 1
                else:
                    count += 1
                    break
            newgrid[i][j] *= count
                
            count = 0
            for k in range(i+1,n):
                if grid[k][j] < x:
                    count += 1
                else:
                    count += 1
                    break
            newgrid[i][j] *= count
            
Max = -1
for i in range(n):
    for j in range(m):
        if newgrid[i][j] > Max:
            Max = newgrid[i][j]

print(Max)
