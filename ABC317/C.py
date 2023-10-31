n,m=map(int,input().split())
table=[[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a,b,c=map(int,input().split())
    table[a-1][b-1]=c
    table[b-1][a-1]=c

route=[i for i in range(n)]

ans=0
def search(route,v,p):
    global ans
    ans=max(ans,v)
    if len(route)>0:
        for dest in route:
            if table[p][dest]:
                r = [x for x in route if x != dest]
                search(r,v+table[p][dest],dest)
    
for i in range(n):
    r=[x for x in route if x != i]
    search(r,0,i)
    
print(ans)
