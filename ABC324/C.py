a=list(input().split())
n=int(a[0])
t=str(a[1])

s=[]
for i in range(n):
    s.append(input())

ans=[]

for i in range(n):
    miss=0
    j=0
    k=0
    if (len(s[i])-len(t))>1 or (len(s[i])-len(t))<-1 :
        continue
    elif len(s[i])==len(t):
        if t in str(s[i]):
            ans.append(i)
            continue
        while j < len(s[i]):
            if t[j]!=s[i][j]:
                miss+=1
                if miss>1:
                    break
            j+=1
    elif len(s[i])==(len(t)+1):
        while j < len(t):
            if s[i][k]==t[j]:
                j+=1
                k+=1
            else:
                miss+=1
                if miss>1:
                    break
                k+=1
    elif len(s[i])+1==len(t):
        while j < len(s[i]):
            if s[i][j]==t[k]:
                j+=1
                k+=1
            else:
                miss+=1
                if miss>1:
                    break
                k+=1
    if miss<2:
        ans.append(i)

print(len(ans))
for a in ans:
    print(str(a+1),end=" ")
print()