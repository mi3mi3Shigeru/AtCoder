n,m= map(int, input().split())
a = list(map(int,input().split()))

s=[]
for i in range(n):
    s.append(list(map(str,input())))

score=[i+1 for i in range(n)]
for i in range(n):
    for j in range(m):
        if s[i][j]=='o':
            score[i]+=a[j]


max_score=max(score)
b=list(enumerate(a))
b.sort(key=lambda x:x[1],reverse=True)

ans=[0 for _ in range(n)]
for i in range(n):
    t=score[i]
    for j in range(m):
        if s[i][b[j][0]]=='o':
            continue
        if t<max_score:
            t+=b[j][1]
            ans[i]+=1
            
for i in ans:
    print(str(i))


