n,m=map(int, input().split())
S=input()
c=list(map(int, input().split()))

s=[char for char in S]

a=[[] for _ in range(m)]
for i in range(n):
    a[c[i]-1].append(i)

ans=s.copy()
for b in a:
    for i in range(len(b)-1,0,-1):
        ans[b[i]]=s[b[i-1]]
    ans[b[0]]=s[b[len(b)-1]]

for i in ans:
    print(i,end="")