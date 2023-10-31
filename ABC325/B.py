n=int(input())
w=[]
x=[]

for i in range(n):
    t1,t2=map(int,input().split())
    w.append(t1)
    x.append(t2)

ans=0
for i in range(24):
    result=0
    for j in range(n):
        time=(i+x[j])%24
        if time< 18:
            if time >8:
                result+=w[j]
    ans=max(ans,result)
print(ans)