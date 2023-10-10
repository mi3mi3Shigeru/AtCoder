n,h,x=map(int, input().split())
p = list(map(int,input().split()))

ans=""
for i in range(n):
    if h+p[i]>=x:
        ans=i+1
        break
    
print(ans)