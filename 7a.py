total = 0

def dfs(temp):
    global total
    val = 0
    for i in temp:
        if type(temp[i]) == int:
            val += temp[i]
        else:
            val += dfs(temp[i])
    if val <= 100000:
        total += val
    return val

#size = {}
stack = []
#direc = ['/']
adj = {'/':{}}
l = adj
while True:
    s = input().split()
    if s == ['-1']:
        break
    if s[0] == '$':
        if s[1] == 'cd':
            if s[2] == '/':
                stack = ['/']
                l = adj['/']
            elif s[2] == '..':
                stack.pop()
                l = adj
                for i in stack:
                    l = l[i]
            else:
                if s[2] not in l:
                    l[s[2]] = {}
                stack.append(s[2])
                l = l[s[2]]
    elif s[0] == 'dir':
        if s[1] not in l:
            l[s[1]] = {}
    else:
        if s[1] not in l:
            l[s[1]] = int(s[0])


dfs(adj)

print(total)



                
            
