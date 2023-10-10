n=int(input())
ans="1"
l=[]
for i in range(1,10):
    if n%i==0:
        l.append(i)

for i in range(1,n+1):
    k="-"
    for j in l:
        if i%(n//j)==0:
            k=str(j)
            break
            
    ans+=k
print(ans)