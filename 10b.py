clock = 0
val = 1
string = ''
while True:
    s = input().split()
    if s == ['-1']:
        break
    if s[0] == 'noop':
        if clock % 40 in (val, val-1, val+1):
            string += '#'
        else:
            string += '.'        
        clock += 1
        if clock == 240:
            break
    else:
        if clock % 40 in (val, val-1, val+1):
            string += '#'
        else:
            string += '.'        
        clock += 1
        if clock == 240:
            break
        
        if clock % 40 in (val, val-1, val+1):
            string += '#'
        else:
            string += '.'        
        clock += 1
        if clock == 240:
            break
        val += int(s[1])

for i in range(6):
    print(string[40 * i:40 * (i+1)])
    
