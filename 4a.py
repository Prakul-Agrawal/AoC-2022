count = 0
while True:
    s = input().split(',')
    if s == ['-1']:
        break
    a,b = list(map(int,s[0].split('-')))
    c,d = list(map(int,s[1].split('-')))
    if a < c:
        if b >= d:
            count += 1
    elif a == c:
        count += 1
    else:
        if b <= d:
            count += 1
print(count)
