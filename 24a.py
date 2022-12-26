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

layer = {(-1,0)}
minute = 1
while True:
    new_layer = set()
    for row,col in layer:
        for new_row, new_col in ((row,col),(row-1,col),(row+1,col),(row,col-1),(row,col+1)):
            if new_row == height and new_col == length - 1:
                print(minute)
                break
            if 0 <= new_row < height and 0 <= new_col < length and \
               grid[new_row][(new_col + minute) % length] != '<' and \
               grid[new_row][(new_col - minute) % length] != '>' and \
               grid[(new_row + minute) % height][new_col] != '^' and \
               grid[(new_row - minute) % height][new_col] != 'v':
                new_layer.add((new_row,new_col))
        else:
            continue
        break
    else:
        layer = new_layer
        layer.add((-1,0))
        minute += 1
        continue
    break
    



