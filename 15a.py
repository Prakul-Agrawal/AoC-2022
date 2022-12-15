l = []
while True:
    s = input().split()
    if s == ["-1"]:
        break
    a = tuple(map(int,(s[2].strip("x=,"),s[3].strip("y=:"),
                       s[8].strip("x=,"),s[9].strip("y="))))
    dis = abs(a[0]-a[2]) + abs(a[1]-a[3])
    l.append((a[0],a[1],dis,a[2],a[3]))

count = 0
val = 2000000

row = []

for i in l:
    dis = i[2] - abs(val - i[1])
    if dis >= 0:
        row.append((i[0]-dis,i[0]+dis))

row.sort()

merge = [row[0]]

for i in range(1,len(row)):
    temp = merge.pop()
    if row[i][0] <= temp[1]:
        new = (temp[0], max(temp[1],row[i][1]))
        merge.append(new)
    else:
        merge.append(temp)
        merge.append(row[i])

for i in merge:
    count += i[1] - i[0] + 1

x = set()
for i in l:
    if i[4] == val:
        for j in merge:
            if j[0] <= i[3] <= j[1] and i[3] not in x:
                count -= 1
                x.add(i[3])
                break

print(count)
