n=int(input())
a=[]
for i in range(n):
    temp=list(map(int,input().split()))
    a.append(temp)
    
a=sorted(a, key=lambda x: x[1],reverse=True)

flavor=a[0][0]
ans=a[0][1]

for i in range(1,n):
    score=a[0][1]
    if a[i][0]==flavor:
        score+=a[i][1]//2
    else:
        score+=a[i][1]
    ans=max(ans,score)
    
print(ans)