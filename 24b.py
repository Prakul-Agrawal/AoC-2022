def shortest(start,end):
    global minute
    layer = {start}
    while True:
        new_layer = set()
        for row,col in layer:
            for new_row, new_col in ((row,col),(row-1,col),(row+1,col),(row,col-1),(row,col+1)):
                if new_row == end[0] and new_col == end[1]:
                    return
                if 0 <= new_row < height and 0 <= new_col < length and \
                   grid[new_row][(new_col + minute) % length] != '<' and \
                   grid[new_row][(new_col - minute) % length] != '>' and \
                   grid[(new_row + minute) % height][new_col] != '^' and \
                   grid[(new_row - minute) % height][new_col] != 'v':
                    new_layer.add((new_row,new_col))
        layer = new_layer
        layer.add(start)
        minute += 1

grid = []

while True:
    s = input()
    if s == '-1':
        break
    grid.append(s[1:-1])

grid.pop()
grid.pop(0)

length = len(grid[0])
height = len(grid)

minute = 1
shortest((-1,0),(height,length-1))
shortest((height,length-1),(-1,0))
shortest((-1,0),(height,length-1))
print(minute)


    



