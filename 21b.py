def dfs(key):
    temp = d[key]
    if temp[0] != -1:
        if key == 'humn':
            dependant[key] = 1
        else:
            dependant[key] = 0
        return d[key][0]
    a = dfs(temp[1])
    b = dfs(temp[2])
    if dependant[temp[1]] or dependant[temp[2]]:
        dependant[key] = 1
    else:
        dependant[key] = 0
    if temp[3] == '+':
        d[key][0] = a + b
        return a + b
    elif temp[3] == '-':
        d[key][0] = a - b
        return a - b
    elif temp[3] == '*':
        d[key][0] = a * b
        return a * b
    else:
        d[key][0] = a // b
        return a // b

def findval(parent,val):
    if parent == 'humn':
        return val
    if d[parent][3] == '+':
        if dependant[d[parent][1]]:
            return findval(d[parent][1], val - d[d[parent][2]][0])
        else:
            return findval(d[parent][2], val - d[d[parent][1]][0])
    elif d[parent][3] == '*':
        if dependant[d[parent][1]]:
            return findval(d[parent][1], val // d[d[parent][2]][0])
        else:
            return findval(d[parent][2], val // d[d[parent][1]][0])
    elif d[parent][3] == '-':
        if dependant[d[parent][1]]:
            return findval(d[parent][1], val + d[d[parent][2]][0])
        else:
            return findval(d[parent][2], d[d[parent][1]][0] - val)
    else:
        if dependant[d[parent][1]]:
            return findval(d[parent][1], val * d[d[parent][2]][0])
        else:
            return findval(d[parent][2], d[d[parent][1]][0] // val)
            

d = {}
dependant = {}
while True:
    s = input().split()
    if s == ['-1']:
        break
    s[0] = s[0][:-1]
    if len(s) == 2:
        x = [int(s[1]),'','','']
    else:
        x = [-1,s[1],s[3],s[2]]
    d[s[0]] = x

dfs('root')

if dependant[d['root'][1]]:
    print(findval(d['root'][1],d[d['root'][2]][0]))
else:
    print(findval(d['root'][2],d[d['root'][1]][0]))

    


