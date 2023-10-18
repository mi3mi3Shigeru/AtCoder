n,m= map(int, input().split())
a = list(map(int,input().split()))
d=[0 for _ in range(n)]
for i in range(m):
    d[a[i]-1]=1

ans=[0 for _ in range(n)]
for i in range(n):
    for j in range(n-i):
        if d[i+j]==1:
            ans[i]=j
            break

for a in ans:
    print(a)