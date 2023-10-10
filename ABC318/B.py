n=int(input())
sheet=[]
for i in range(n):
    sheet.append(list(map(int,input().split())))

max_n=100
table= [[0 for _ in range(max_n)] for _ in range(max_n)]

for i in sheet:
    for x in range(i[0],i[1]):
        for y in range(i[2],i[3]):
            table[x][y]=1
            
ans=0
for i in range(max_n):
    for j in range(max_n):
        if table[i][j]==1:
            ans+=1

print(ans)