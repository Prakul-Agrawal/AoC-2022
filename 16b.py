def dfs(bits,pos,visited,time,score):
    time -= 1
    bits = bits + (1 << pos)
    score += pressure[pos] * time
    final[bits] = max(final.get(bits,0),score)
    visited[pos] = 1
    for i in range(length):
        if visited[i] == 0 and graph[pos][i] < time:
            dfs(bits,i,visited,time-graph[pos][i],score)
    visited[pos] = 0
    return

d = {}
l = []
INF = 999
while True:
    s = input().split()
    if s == ['-1']:
        break
    x = dict([[i.strip(","),1] for i in s[9:]])
    val = int(s[4].strip("rate=;"))
    d[s[1]] = [val,x]
    l.append(s[1])

for i in l:
    if d[i][0] == 0 and i != 'AA':
        x = d[i][1]
        y = list(x.keys())
        for a in range(len(y)):
            for b in range(a+1,len(y)):
                temp = min(d[y[a]][1].get(y[b],INF),x[y[a]] + x[y[b]])
                d[y[a]][1][y[b]] = temp
                d[y[b]][1][y[a]] = temp
        for a in y:
            del(d[a][1][i])
        del[d[i]]
        
length = len(d.keys())
WordToNum = dict(zip(d.keys(),[i for i in range(length)]))
NumToWord = dict(zip([i for i in range(length)],d.keys()))
pressure = [i[0] for i in d.values()]

graph = [[INF for j in range(length)] for i in range(length)]

for i in range(length):
    x = d[NumToWord[i]][1]
    for j in x:
        graph[i][WordToNum[j]] = x[j]
    graph[i][i] = 0

for k in range(length):
    for i in range(length):
        for j in range(length):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

start = WordToNum['AA']
final = {}
visited = [0 for i in range(length)]

dfs(0,start,visited,27,0)

Max = 0
position = 1 << start
x = list(final.keys())
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] & x[j] == position:
            Max = max(Max,final[x[i]] + final[x[j]])

print(Max)
