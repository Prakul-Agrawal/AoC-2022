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

lists = []
while True:
    s1 = input()
    if s1 == '-1':
        break
    s2 = input()
    input()
    l = eval(s1)
    k = eval(s2)
    lists.append(l)
    lists.append(k)

lists.append([[2]])
lists.append([[6]])
n = len(lists)

for i in range(n-1): #sorting
    for j in range(n-1-i):
        p = iterate(lists[j],lists[j+1])
        if p == 0:
            lists[j],lists[j+1] = lists[j+1],lists[j]

prod = 1
for i in range(n):
    if lists[i] == [[2]] or lists[i] == [[6]]:
        prod *= i + 1
    
print(prod)
