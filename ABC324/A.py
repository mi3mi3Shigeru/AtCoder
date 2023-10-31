n=input()
a=list(map(int,input().split()))
ans="Yes"
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        ans="No"
        break
print(ans)