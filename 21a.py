def dfs(key):
    temp = d[key]
    if temp[0] != -1:
        return d[key][0]
    a = dfs(temp[1])
    b = dfs(temp[2])
    if temp[3] == '+':
        return a + b
    elif temp[3] == '-':
        return a - b
    elif temp[3] == '*':
        return a * b
    else:
        return int(a / b)

d = {}
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

print(dfs('root'))


