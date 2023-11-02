m=int(input())
s=[[],[],[]]
for i in range(3):
    t=str(input())
    for j in range(len(t)):
        s[i].append(int(t[j]))
        
table=[[]for _ in range(10)]

for i in range(3):
    temp = [[]for _ in range(10)] 
    for j in range(m):
        temp[s[i][j]].append(j)
    for k in range(10):
        table[k].append(temp[k])

import itertools
elements = [0,1,2]
permutations = itertools.permutations(elements)
order_list = list(permutations)

ans=-1
for i in table:
    for order in order_list:
        time=-1
        for j in order:
            if len(i[j])==0:
                time=-1
                break
            else:
                better_time=1000
                for k in range(len(i[j])):
                    temp=i[j][k]
                    while(time>=temp):
                        temp+=m
                    better_time=min(better_time,temp)
                time=better_time
                
        if ans<0 and time>0:
            ans=time
        elif time>0 and ans>0:
            ans=min(ans,time)
print(ans)