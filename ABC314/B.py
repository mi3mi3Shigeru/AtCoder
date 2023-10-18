n=int(input())
c=[]
a=[]
for i in range(n):
    c.append(int(input()))
    a.append(list(map(int,input().split())))
x=int(input())

table=[[] for _ in range(37)]

for i in range(n):
    for j in range(len(a[i])):    
        table[a[i][j]].append(i)

b=table[x]
min_bets=100
for i in b:
    min_bets=min(min_bets,c[i])
k=[]
for i in b:
    if c[i]==min_bets:
        k.append(i)

print(len(k))
for i in k:
    print(str(i+1),"",end="")
    