s=input()
ans=1
for i in range(len(s)):
    for j in range(len(s),0,-1):
        word=s[i:i+j]
        rev=""
        for k in range(len(word),0,-1):
            rev+=word[k-1]
        if word==rev:
            ans=max(ans,len(word))

print(ans)