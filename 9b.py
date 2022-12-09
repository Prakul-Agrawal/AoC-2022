grid = [[0 for i in range(2000)] for j in range(2000)]

T = [[1000,1000] for i in range(10)]
grid[1000][1000] = 1

while True:
    s = input().split()
    if s == ['-1']:
        break
    for i in range(int(s[1])):
        if s[0] == 'U':
            T[0][0] -= 1
        elif s[0] == 'D':
            T[0][0] += 1
        elif s[0] == 'R':
            T[0][1] += 1
        else:
            T[0][1] -= 1

        for j in range(1,10):    
            if abs(T[j-1][0] - T[j][0]) < 2 and abs(T[j-1][1] - T[j][1]) < 2:
                break

            if T[j-1][0] - T[j][0] == 2:
                if T[j-1][1] - T[j][1] == 2:
                    T[j][0] += 1
                    T[j][1] += 1
                elif T[j-1][1] - T[j][1] == -2:
                    T[j][0] += 1
                    T[j][1] -= 1
                elif T[j-1][1] - T[j][1] == 1:
                    T[j][0] += 1
                    T[j][1] += 1
                elif T[j-1][1] - T[j][1] == -1:
                    T[j][0] += 1
                    T[j][1] -= 1
                else:
                    T[j][0] += 1
            elif T[j-1][0] - T[j][0] == -2:
                if T[j-1][1] - T[j][1] == 2:
                    T[j][0] -= 1
                    T[j][1] += 1
                elif T[j-1][1] - T[j][1] == -2:
                    T[j][0] -= 1
                    T[j][1] -= 1
                elif T[j-1][1] - T[j][1] == 1:
                    T[j][0] -= 1
                    T[j][1] += 1
                elif T[j-1][1] - T[j][1] == -1:
                    T[j][0] -= 1
                    T[j][1] -= 1
                else:
                    T[j][0] -= 1
            elif T[j-1][1] - T[j][1] == 2:
                if T[j-1][0] - T[j][0] == 1:
                    T[j][0] += 1
                    T[j][1] += 1
                elif T[j-1][0] - T[j][0] == -1:
                    T[j][0] -= 1
                    T[j][1] += 1
                else:
                    T[j][1] += 1
            elif T[j-1][1] - T[j][1] == -2:
                if T[j-1][0] - T[j][0] == 1:
                    T[j][0] += 1
                    T[j][1] -= 1
                elif T[j-1][0] - T[j][0] == -1:
                    T[j][0] -= 1
                    T[j][1] -= 1
                else:
                    T[j][1] -= 1
        

        grid[T[9][0]][T[9][1]] = 1

count = 0
for i in grid:
    for j in i:
        if j == 1:
            count += 1

print(count)
        

