count = 0
while True:
    s = input().split(',')
    if s == ['-1']:
        break
    a,b = list(map(int,s[0].split('-')))
    c,d = list(map(int,s[1].split('-')))
    if b >= c and d >= a:
        count += 1
print(count)
