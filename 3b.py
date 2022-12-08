total = 0
while True:
    a = [0 for i in range(52)]
    b = [0 for i in range(52)]
    c = [0 for i in range(52)]
    s1 = input()
    if s1 == '-1':
        break
    s2 = input()
    s3 = input()
    for i in s1:
        if i.islower():
            a[ord(i) - ord('a')] += 1
        else:
            a[ord(i) - ord('A') + 26] += 1
    for i in s2:
        if i.islower():
            b[ord(i) - ord('a')] += 1
        else:
            b[ord(i) - ord('A') + 26] += 1
    for i in s3:
        if i.islower():
            c[ord(i) - ord('a')] += 1
        else:
            c[ord(i) - ord('A') + 26] += 1
    for i in range(52):
        if a[i] > 0 and b[i] > 0 and c[i] > 0:
            total += i + 1
            break
print(total)
    
