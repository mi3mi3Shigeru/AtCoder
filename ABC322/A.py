n=int(input())
s=input()
ans="-1"
for i in range(len(s)-2):
    if str(s[i:i+3])=="ABC":
        ans=i+1
        break
    
print(ans)