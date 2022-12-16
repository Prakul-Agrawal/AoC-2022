def flowval(time,bits):
    total = 0
    for i in range(length):
        total += pressure[i] * time * (bits >> i & 1)
    return total

def calc(cur_pos, bits, time):
    if time == 0:
        return 0
    if bits >> cur_pos & 1 == 0:
        if dp[cur_pos][bits + (1 << cur_pos)][time-1] == -1:
            dp[cur_pos][bits + (1 << cur_pos)][time-1] = calc(cur_pos, bits + (1 << cur_pos), time-1)
        dp[cur_pos][bits][time] = dp[cur_pos][bits + (1 << cur_pos)][time-1] + flowval(1,bits)
    else:
        dp[cur_pos][bits][time] = flowval(time,bits)
        for i in range(length):
            if i != cur_pos:
                temp = graph[cur_pos][i]
                if time - temp > 0:
                    if dp[i][bits][time-temp] == -1:
                        dp[i][bits][time-temp] = calc(i, bits, time-temp)
                    dp[cur_pos][bits][time] = max(dp[cur_pos][bits][time],dp[i][bits][time-temp] + flowval(temp,bits))
    return dp[cur_pos][bits][time]
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

#for i in graph:
#    print(i)

#bits = [0 for i in range(length)]

dp = [[[-1 for k in range(31)] for j in range(1 << length)] for i in range(length)]


start = WordToNum['AA']

print(calc(start,1 << start,30))




    
