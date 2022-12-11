count = [0 for i in range(8)]

values = [[63, 84, 80, 83, 84, 53, 88, 72],
          [67, 56, 92, 88, 84],
          [52],
          [59, 53, 60, 92, 69, 72],
          [61, 52, 55, 61],
          [79, 53],
          [59, 86, 67, 95, 92, 77, 91],
          [58, 83, 89]]

div = [13,11,2,5,7,3,19,17]
prod = 1
for i in div:
    prod *= i
true = [4,5,3,5,7,0,4,2]
false = [7,3,1,6,2,6,0,1]

for i in range(10000):
    #if i % 1000 == 0:
        #print(i)
    for j in range(8):
        while values[j] != []:
            count[j] += 1
            x = values[j].pop(0)
            if j == 0:
                x *= 11
            elif j == 1:
                x += 4
            elif j == 2:
                x *= x
            elif j == 3:
                x += 2
            elif j == 4:
                x += 3
            elif j == 5:
                x += 1
            elif j == 6:
                x += 5
            else:
                x *= 19
            x %= prod
            if x % div[j] == 0:
                values[true[j]].append(x)
            else:
                values[false[j]].append(x)

count.sort()
print(count[-1] * count[-2])


        
    
