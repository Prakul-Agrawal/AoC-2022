def change_pos(grid_no,pos,direction,change):
    if direction == 0:
        if pos[1] == 49:
            temp_grid_no = change[0][0]
            temp_pos = change[0][1]
            temp_dir = change[0][2]
        else:
            temp_grid_no = grid_no
            temp_pos = (pos[0],pos[1]+1)
            temp_dir = direction
        if grid[temp_grid_no][temp_pos[0]][temp_pos[1]] == '#':
            return -1
        grid_no = temp_grid_no
        pos = temp_pos
        direction = temp_dir
    elif direction == 1:
        if pos[0] == 49:
            temp_grid_no = change[1][0]
            temp_pos = change[1][1]
            temp_dir = change[1][2]
        else:
            temp_grid_no = grid_no
            temp_pos = (pos[0]+1,pos[1])
            temp_dir = direction
        if grid[temp_grid_no][temp_pos[0]][temp_pos[1]] == '#':
            return -1
        grid_no = temp_grid_no
        pos = temp_pos
        direction = temp_dir
    elif direction == 2:
        if pos[1] == 0:
            temp_grid_no = change[2][0]
            temp_pos = change[2][1]
            temp_dir = change[2][2]
        else:
            temp_grid_no = grid_no
            temp_pos = (pos[0],pos[1]-1)
            temp_dir = direction
        if grid[temp_grid_no][temp_pos[0]][temp_pos[1]] == '#':
            return -1
        grid_no = temp_grid_no
        pos = temp_pos
        direction = temp_dir
    else:
        if pos[0] == 0:
            temp_grid_no = change[3][0]
            temp_pos = change[3][1]
            temp_dir = change[3][2]
        else:
            temp_grid_no = grid_no
            temp_pos = (pos[0]-1,pos[1])
            temp_dir = direction
        if grid[temp_grid_no][temp_pos[0]][temp_pos[1]] == '#':
            return -1
        grid_no = temp_grid_no
        pos = temp_pos
        direction = temp_dir
    return (grid_no,pos,direction)

def make_move(steps,direction,pos,grid_no):
    while steps:
        if grid_no == 0:
            temp = change_pos(grid_no,pos,direction,
                              ((1,(pos[0],0),0),(2,(0,pos[1]),1),(3,(49-pos[0],0),0),(5,(pos[1],0),0)))
        elif grid_no == 1:
            temp = change_pos(grid_no,pos,direction,
                              ((4,(49-pos[0],49),2),(2,(pos[1],49),2),(0,(pos[0],49),2),(5,(49,pos[1]),3)))
        elif grid_no == 2:
            temp = change_pos(grid_no,pos,direction,
                              ((1,(49,pos[0]),3),(4,(0,pos[1]),1),(3,(0,pos[0]),1),(0,(49,pos[1]),3)))
        elif grid_no == 3:
            temp = change_pos(grid_no,pos,direction,
                              ((4,(pos[0],0),0),(5,(0,pos[1]),1),(0,(49-pos[0],0),0),(2,(pos[1],0),0)))
        elif grid_no == 4:
            temp = change_pos(grid_no,pos,direction,
                              ((1,(49-pos[0],49),2),(5,(pos[1],49),2),(3,(pos[0],49),2),(2,(49,pos[1]),3)))
        else:
            temp = change_pos(grid_no,pos,direction,
                              ((4,(49,pos[0]),3),(1,(0,pos[1]),1),(0,(0,pos[0]),1),(3,(49,pos[1]),3)))

        if temp == -1:
            return grid_no,pos,direction
        grid_no,pos,direction = temp
        steps -= 1

    return grid_no,pos,direction

def change_direction(direction,let):
    if let == 'R':
        return (direction + 1) % 4
    return (direction - 1) % 4
            
                
                

grid = [[] for i in range(6)]

for i in range(50):
    s = input().strip()
    grid[0].append(s[:50])
    grid[1].append(s[50:])
for i in range(50):
    s = input().strip()
    grid[2].append(s)
for i in range(50):
    s = input().strip()
    grid[3].append(s[:50])
    grid[4].append(s[50:])
for i in range(50):
    s = input().strip()
    grid[5].append(s)


cur_grid = 0
cur_pos = (0,0)
cur_dir = 0
input()
s = input()
move = []
letters = []

temp = ''
for i in s:
    if i not in ('L','R'):
        temp += i
    else:
        move.append(int(temp))
        letters.append(i)
        temp = ''
move.append(int(temp))

iterations = len(letters)

for i in range(iterations):
    cur_grid, cur_pos, cur_dir = make_move(move[i],cur_dir,cur_pos,cur_grid)
    cur_dir = change_direction(cur_dir,letters[i])
cur_grid, cur_pos, cur_dir = make_move(move[-1],cur_dir,cur_pos,cur_grid)

#print(cur_grid, cur_pos, cur_dir) #can calculate the row, col and direction from this

total = 0
if cur_grid == 0:
    total += 200
elif cur_grid == 1:
    total += 400
elif cur_grid == 2:
    total += 50200
elif cur_grid == 3:
    total += 100000
elif cur_grid == 4:
    total += 100200
else:
    total += 150000
total += (cur_pos[0] + 1) * 1000 + (cur_pos[1] + 1) * 4 + cur_dir
print(total)

    


