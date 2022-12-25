q = 0
d = {'0':0,'1':1,'2':2,'-':-1,'=':-2}
while True:
    s = input()
    if s == '-1':
        break
    length = len(s)
    for i in range(length):
        q += pow(5,length-1-i)*d[s[i]]

final = ''
while q:
    q,r = divmod(q,5)
    if r < 3:
        final += str(r)
    else:
        q += 1
        if r == 3:
            final += '='
        else:
            final += '-'

print(final[::-1])
