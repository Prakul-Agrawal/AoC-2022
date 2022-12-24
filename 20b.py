l = []
while True:
    s = int(input())
    if s == 999999:
        break
    l.append(s*811589153)

array = list(enumerate(l))

length = len(array)

for t in range(10):
    for i in range(length):
        for j in range(length):
            if array[j][0] == i:
                val = array.pop(j)
                pos = (val[1] + j) % (length - 1)
                if pos == 0:
                    array.append(val)
                else:
                    array.insert(pos, val)
                break

for i in range(length):
    if array[i][1] == 0:
        print(sum(array[(i + j) % length][1] for j in (1000,2000,3000)))
        break
