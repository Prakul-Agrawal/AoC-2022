from collections import defaultdict

locations = set()
y = 0
while True:
    s = input()
    if s == '-1':
        break
    for x in range(len(s)):
        if s[x] == '#':
            locations.add((x,y))
    y += 1

adj = ((-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0))
movement = ((-1,-1),(0,-1),(1,-1),(-1,1),(0,1),(1,1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1))

t = 0
while True:
    t += 1
    new_locations = defaultdict(list)

    for pos in locations:
        if any((pos[0] + new[0], pos[1] + new[1]) in locations for new in adj):
            for i in range(4):
                for change in (movement[3*(t - 1 + i) % 12 + j] for j in range(3)):
                    if (pos[0] + change[0], pos[1] + change[1]) in locations:
                        break
                else:
                    change = movement[3*(t - 1 + i) % 12 + 1]
                    new_locations[(pos[0] + change[0], pos[1] + change[1])].append(pos)
                    break

    if len(new_locations) == 0:
        print(t)
        break
    for x in new_locations:
        if len(new_locations[x]) == 1:
            locations.remove(new_locations[x][0])
            locations.add(x)
