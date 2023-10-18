n,m= map(int, input().split())
a = list(map(int,input().split()))
d=[0 for _ in range(n)]
for i in range(m):
    d[a[i]-1]=1

ans=[0 for _ in range(n)]
count=0
for i in range(n,0,-1):
    if d[i-1]==1:
        count=0
    else :
        count+=1
    ans[i-1]=count
    
for a in ans:
    print(a)