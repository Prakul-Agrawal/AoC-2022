S = []
V = 0
while True:
    x = input()
    if x == '':
        if V > S:
            S.append(V)
        V = 0
    elif x == '-1':
        break
    else:
        V += int(x)
S.sort()
print(sum(S[-3:]))
