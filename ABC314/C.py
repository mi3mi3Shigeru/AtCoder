n,m=map(int, input().split())
S=input()
c=list(map(int, input().split()))

s=[char for char in S]
ans=s.copy()

first_index=[-1 for _ in range(m)]
a=first_index.copy()
b=a.copy()


for i in range(n):
    color=c[i]-1
    if a[color]==-1:
        first_index[color]=i
        a[color]=i
    else:
        b[color]=i
        ans[i]=s[a[color]]
        a[color]=b[color]


for j in range(m):
    if b[j]!=-1:
        ans[first_index[j]]=s[a[j]]
        
for i in ans:
    print(i,end="")