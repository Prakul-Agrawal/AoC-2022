#Had to take a hint for this
#Uses geometry
#Uses equation of a line

l = []
while True:
    s = input().split()
    if s == ["-1"]:
        break
    a = tuple(map(int,(s[2].strip("x=,"),s[3].strip("y=:"),
                       s[8].strip("x=,"),s[9].strip("y="))))
    dis = abs(a[0]-a[2]) + abs(a[1]-a[3])
    l.append((a[0],a[1],dis))

a,b = set(),set()
for i in l:
    a.add(i[1]-i[0]+i[2]+1)
    a.add(i[1]-i[0]-i[2]-1)
    b.add(i[1]+i[0]+i[2]+1)
    b.add(i[1]+i[0]-i[2]-1)

for i in a:
    for j in b:
        p = ((j-i)//2,(j+i)//2)
        if 0 < p[0] < 4000000 and 0 < p[1] < 4000000:
            for sensor in l:
                if abs(p[0]-sensor[0]) + abs(p[1]-sensor[1]) <= sensor[2]:
                    break
            else:
                print(4000000*p[0] + p[1])
