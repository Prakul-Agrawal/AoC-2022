def side(direction,xpos,ypos,rock_type):
    if direction == '>':
        if rock_type == 0:
            if grid[xpos][ypos+4] == 0:
                return ypos+1
        elif rock_type == 1:
            if all([1-grid[xpos][ypos+2],1-grid[xpos-1][ypos+1],1-grid[xpos+1][ypos+1]]):
                return ypos+1
        elif rock_type == 2:
            if all([1-grid[xpos+i][ypos+1] for i in range(3)]):
                return ypos+1
        elif rock_type == 3:
            if all([1-grid[xpos+i][ypos+1] for i in range(4)]):
                return ypos+1
        else:
            if all([1-grid[xpos+i][ypos+2] for i in range(2)]):
                return ypos+1
    else:
        if rock_type == 0:
            if grid[xpos][ypos-1] == 0:
                return ypos-1
        elif rock_type == 1:
            if all([1-grid[xpos][ypos-2],1-grid[xpos-1][ypos-1],1-grid[xpos+1][ypos-1]]):
                return ypos-1
        elif rock_type == 2:
            if all([1-grid[xpos][ypos-3],1-grid[xpos+1][ypos-1],1-grid[xpos+2][ypos-1]]):
                return ypos-1
        elif rock_type == 3:
            if all([1-grid[xpos+i][ypos-1] for i in range(4)]):
                return ypos-1
        else:
            if all([1-grid[xpos+i][ypos-1] for i in range(2)]):
                return ypos-1
            
    return ypos

def down(xpos,ypos,rock_type):
    if rock_type == 0:
        if all([1-grid[xpos-1][ypos+i] for i in range(4)]):
            return xpos-1
    elif rock_type == 1:
        if all([1-grid[xpos-2][ypos],1-grid[xpos-1][ypos+1],1-grid[xpos-1][ypos-1]]):
            return xpos-1
    elif rock_type == 2:
        if all([1-grid[xpos-1][ypos-i] for i in range(3)]):
            return xpos-1
    elif rock_type == 3:
        if grid[xpos-1][ypos] == 0:
            return xpos-1
    else:
        if all([1-grid[xpos-1][ypos+i] for i in range(2)]):
            return xpos-1

    return -1
            
def pos(rock_type):
    if rock_type in (0,3,4):        
        return highest + 4, 3
    elif rock_type == 1:
        return highest + 5, 4
    return highest + 4, 5

def fix_rock(rock_type,highest,xpos,ypos):
    if rock_type == 0:
        for i in range(4):
            grid[xpos][ypos+i] = 1
        return max(xpos,highest)
    elif rock_type == 1:
        for i in (1,-1):
            grid[xpos+i][ypos] = 1
            grid[xpos][ypos+i] = 1
        grid[xpos][ypos] = 1
        return max(xpos+1,highest)
    elif rock_type == 2:
        for i in (1,2):
            grid[xpos+i][ypos] = 1
            grid[xpos][ypos-i] = 1
        grid[xpos][ypos] = 1
        return max(xpos+2,highest)
    elif rock_type == 3:
        for i in range(4):
            grid[xpos+i][ypos] = 1
        return max(xpos+3,highest)
    else:
        for i in (0,1):
            for j in (0,1):
                grid[xpos+i][ypos+j] = 1
        return max(xpos+1,highest)

s = input()
length = len(s)

grid = [[1 if (j in (0,8)) else 0 for j in range(9)] for i in range(10000)]

for i in range(7):
    grid[0][i] = 1

highest = 0
rock = 0
point = 0
store = {}
while rock < 1000000000000:
    rock_type = rock % 5
    xpos,ypos = pos(rock_type)
    moving = 1
    key = (rock_type,point)
    if key in store: #took a hint for this cache part
        prev_rock_no,prev_highest = store[key]
        if (int(1e12)-rock)%(rock-prev_rock_no) == 0:
            highest = highest + (int(1e12)-rock)//(rock-prev_rock_no)*(highest-prev_highest)
            break
    else:
        store[key] = (rock,highest)
    while moving:
        ypos = side(s[point],xpos,ypos,rock_type)
        point = (point + 1) % length
        temp_xpos = down(xpos,ypos,rock_type)
        if temp_xpos == -1:
            highest = fix_rock(rock_type,highest,xpos,ypos)
            moving = 0
        else:
            xpos = temp_xpos        
    rock += 1

print(highest)
