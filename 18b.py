l = []
dim = [0,0,0]
while True:
    k = list(map(int,input().split(',')))
    if k == [-1]:
        break
    k = [i+3 for i in k]
    
    l.append(k)
    for i in range(3):
        if k[i] > dim[i]:
            dim[i] = k[i]

for i in range(3):
    dim[i] += 5

grid = [[[0 for z in range(dim[2])] for y in range(dim[1])] for x in range(dim[0])]

for i in l:
    grid[i[0]][i[1]][i[2]] = 2

water = [(0,0,0)]
grid[0][0][0] = 1

#flood fill

total = 0
while water:
    x,y,z = water.pop(0)
    if x > 0:
        if grid[x-1][y][z] == 0:
            grid[x-1][y][z] = 1
            water.append((x-1,y,z))
        elif grid[x-1][y][z] == 2:
            total += 1
    if y > 0:
        if grid[x][y-1][z] == 0:
            grid[x][y-1][z] = 1
            water.append((x,y-1,z))
        elif grid[x][y-1][z] == 2:
            total += 1
    if z > 0:
        if grid[x][y][z-1] == 0:
            grid[x][y][z-1] = 1
            water.append((x,y,z-1))
        elif grid[x][y][z-1] == 2:
            total += 1
    if x < dim[0]-1:
        if grid[x+1][y][z] == 0:
            grid[x+1][y][z] = 1
            water.append((x+1,y,z))
        elif grid[x+1][y][z] == 2:
            total += 1
    if y < dim[1]-1:
        if grid[x][y+1][z] == 0:
            grid[x][y+1][z] = 1
            water.append((x,y+1,z))
        elif grid[x][y+1][z] == 2:
            total += 1
    if z < dim[2]-1:
        if grid[x][y][z+1] == 0:
            grid[x][y][z+1] = 1
            water.append((x,y,z+1))
        elif grid[x][y][z+1] == 2:
            total += 1

print(total)
