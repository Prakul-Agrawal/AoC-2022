stack = [['B','V','S','N','T','C','H','Q'],
          ['W','D','B','G'],
          ['F','W','R','T','S','Q','B'],
          ['L','G','W','S','Z','J','D','N'],
          ['M','P','D','V','F'],
          ['F','W','J'],
          ['L','N','Q','B','J','V'],
          ['G','T','R','C','J','Q','S','N'],
          ['J','S','Q','C','W','D','M']]

while True:
    s = input().split()
    if s == ['-1']:
        break
    stack[int(s[5])-1].extend(stack[int(s[3])-1][-int(s[1]):])
    del(stack[int(s[3])-1][-int(s[1]):])

final = ''
for i in range(9):
    final += stack[i][-1:][0]

print(final)
