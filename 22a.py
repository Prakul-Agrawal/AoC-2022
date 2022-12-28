def change_pos(grid_no,pos,direction,*change_grid):
    if direction == 0:
        if pos[1] == 49:
            temp_pos = (pos[0],0)
            temp_grid_no = change_grid[0]
        else:
            temp_pos = (pos[0],pos[1]+1)
            temp_grid_no = grid_no
        if grid[temp_grid_no][temp_pos[0]][temp_pos[1]] == '#':
            return -1
        grid_no = temp_grid_no
        pos = temp_pos
    elif direction == 1:
        if pos[0] == 49:
            temp_pos = (0,pos[1])
            temp_grid_no = change_grid[1]
        else:
            temp_pos = (pos[0]+1,pos[1])
            temp_grid_no = grid_no
        if grid[temp_grid_no][temp_pos[0]][temp_pos[1]] == '#':
            return -1
        grid_no = temp_grid_no
        pos = temp_pos
    elif direction == 2:
        if pos[1] == 0:
            temp_pos = (pos[0],49)
            temp_grid_no = change_grid[2]
        else:
            temp_pos = (pos[0],pos[1]-1)
            temp_grid_no = grid_no
        if grid[temp_grid_no][temp_pos[0]][temp_pos[1]] == '#':
            return -1
        grid_no = temp_grid_no
        pos = temp_pos
    else:
        if pos[0] == 0:
            temp_pos = (49,pos[1])
            temp_grid_no = change_grid[3]
        else:
            temp_pos = (pos[0]-1,pos[1])
            temp_grid_no = grid_no
        if grid[temp_grid_no][temp_pos[0]][temp_pos[1]] == '#':
            return -1
        grid_no = temp_grid_no
        pos = temp_pos
    return (grid_no,pos)

def make_move(steps,direction,pos,grid_no):
    while steps:
        if grid_no == 0:
            temp = change_pos(grid_no,pos,direction,1,2,1,4)
        elif grid_no == 1:
            temp = change_pos(grid_no,pos,direction,0,1,0,1)
        elif grid_no == 2:
            temp = change_pos(grid_no,pos,direction,2,4,2,0)
        elif grid_no == 3:
            temp = change_pos(grid_no,pos,direction,4,5,4,5)
        elif grid_no == 4:
            temp = change_pos(grid_no,pos,direction,3,0,3,2)
        else:
            temp = change_pos(grid_no,pos,direction,5,3,5,3)

        if temp == -1:
            return grid_no,pos
        grid_no,pos = temp
        steps -= 1

    return grid_no,pos

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
    cur_grid, cur_pos = make_move(move[i],cur_dir,cur_pos,cur_grid)
    cur_dir = change_direction(cur_dir,letters[i])
cur_grid, cur_pos = make_move(move[-1],cur_dir,cur_pos,cur_grid)

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

