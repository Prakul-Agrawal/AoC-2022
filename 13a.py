def iterate(l1,l2):
    a,b = len(l1),len(l2)
    for i in range(a):
        if i == b:
            return 0
        if type(l1[i]) == type(l2[i]) == int:
            if l1[i] < l2[i]:
                return 1
            elif l1[i] > l2[i]:
                return 0
        elif type(l1[i]) == type(l2[i]) == list:
            x = iterate(l1[i],l2[i])
            if x == 2:
                continue
            else:
                return x
        elif type(l1[i]) == int:
            temp = [l1[i]]
            x = iterate(temp,l2[i])
            if x == 2:
                continue
            else:
                return x
        elif type(l2[i]) == int:
            temp = [l2[i]]
            x = iterate(l1[i],temp)
            if x == 2:
                continue
            else:
                return x 
    if a < b:
        return 1
    return 2

total = 0
count = 0
while True:
    count += 1
    s1 = input()
    if s1 == '-1':
        break
    s2 = input()
    input()
    l = eval(s1)
    k = eval(s2)
    p = iterate(l,k)
    if p == 1:
        total += count
        #print(count)
    
print(total)
