#hos
from collections import defaultdict
t = int(input())
for i in range(t):
    a = []
    for i in range(10):
        m = input()
        a.append(m)
    
    dict = defaultdict()
    for i in range(10):
        for j in range(10):
            if a[i][j] =="X":
                if i == 0 or j==0 or j == 9 or i == 9:
                    dict[1] = dict.get(1,0)+1
                elif (i == 1 and 1 <= j <= 8) or (i == 8 and 1 <= j <= 8) or(j == 1 and 1 <= i <= 8) or (j == 8 and 1 <= i <= 8):
                    dict[2] = dict.get(2,0)+1
                elif (i == 2 and 2 <= j <= 7) or (i == 7 and 2 <= j <= 7) or(j == 2 and 2 <= i <= 7) or (j == 7 and 2 <= i <= 7):
                    dict[3] = dict.get(3,0)+1
                elif (i == 3 and 3 <= j <= 6) or (i == 6 and 3 <= j <= 6) or(j == 3 and 3 <= i <= 6) or (j == 6 and 3 <= i <= 6):
                    dict[4] = dict.get(4,0)+1
                else:
                    dict[5] = dict.get(5,0)+1
    
    al = 0
    for i,val in dict.items():
        al += i*val

    print(al)


