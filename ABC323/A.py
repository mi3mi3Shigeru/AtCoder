s=input()
flag=True
i=16

while flag:
    if s[i-1]=='1':
        flag=False
        break
    else:
        i-=2
        if i<0:
            break
        
ans=""
if flag:
    ans="Yes"
else:
    ans="No"
print(ans)