n=int(input())
a = list(map(int,input().split()))

b=a.copy()
b.sort()
ans=""
for i in range(n):
    if (b[i]+1)!=b[i+1]:
        ans=b[i]+1
        break
print(ans)