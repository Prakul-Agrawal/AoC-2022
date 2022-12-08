s = input()
length = len(s)
x = s[:13]
val = 13
char = [0 for i in range(26)]
for i in x:
    char[ord(i) - ord('a')] += 1
for i in range(13,length):
    val += 1
    char[ord(s[i]) - ord('a')] += 1
    x += s[i]
    for j in x:
        if char[ord(j) - ord('a')] > 1:
            break
    else:
        break
    char[ord(x[0]) - ord('a')] -= 1
    x = x[1:]

print(val)
