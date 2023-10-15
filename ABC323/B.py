n=int(input())
s=[]
for i in range(n):
    s.append(list(map(str,input())))

score=[0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j]=='o':
            score[i]+=1

order=list(enumerate(score))
order.sort(key=lambda x:x[1],reverse=True)
for i in range(n):
    print(str(order[i][0]+1),"",end="")
    
print()