score = 0
while True:
    x = input()
    if x == '-1':
        break
    p,q = x.split()
    p = ord(p) - ord('A')
    q = ord(q) - ord('X')

    if p == q:
        score += 3 + q + 1
    elif p - q == 1 or q - p == 2:
        score += q + 1
    else:
        score += 6 + q + 1
    
print(score)
