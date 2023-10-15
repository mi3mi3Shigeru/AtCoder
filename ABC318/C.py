import math
n,d,p=map(int, input().split())
f=list(map(int,input().split()))

fee=f.copy()
fee.sort()

regular_price=[fee[0]]
for i in range(1,n):
    regular_price.append(regular_price[i-1]+fee[i])
    
k=math.ceil(n/d)

ans=k*p
for i in range(k):
    ans=min(ans,regular_price[n-1-i*d]+i*p)
print(ans)