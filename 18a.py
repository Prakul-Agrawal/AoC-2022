l = [0 for i in range(1000000)]

while True:
    k = list(map(int,input().split(',')))
    if k == [-1]:
        break
    l[k[0]*10000+k[1]*100+k[2]] = 1
    
total = 0
for i in range(500000):
    if l[i] == 0:
        continue
    val = 6
    if l[i-10000]:
        val -= 1
    if l[i+10000]:
        val -= 1
    if l[i-100]:
        val -= 1
    if l[i+100]:
        val -= 1
    if l[i-1]:
        val -= 1
    if l[i+1]:
        val -= 1
    total += val

print(total)
