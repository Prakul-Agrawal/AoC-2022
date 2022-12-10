clock = 0
val = 1
total = 0
while True:
    s = input().split()
    if s == ['-1']:
        break
    if s[0] == 'noop':
        clock += 1
        if clock % 40 == 20 and clock <= 220:
            total += clock * val
    else:
        clock += 1
        if clock % 40 == 20 and clock <= 220:
            total += clock * val
        clock += 1
        if clock % 40 == 20 and clock <= 220:
            total += clock * val
        val += int(s[1])

print(total)
    
