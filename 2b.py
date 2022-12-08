score = 0
while True:
    x = input()
    if x == '-1':
        break
    p,q = x.split()
    p = ord(p) - ord('A')
    q = ord(q) - ord('X')

    if q == 1:
        score += p + 4
    elif q == 0:
        score += (p - 1) % 3 + 1
    else:
        score += (p + 1) % 3 + 7
    
print(score)
