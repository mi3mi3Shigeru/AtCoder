import sys

sys.setrecursionlimit(1000000)

h,w=map(int,input().split())
table=[[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    s=input()
    for j in range(w):
        if s[j]=='#':
            table[i][j]=1

t=table.copy()
ans=0
def dfs(x,y):
    global t,w,h
    if t[y][x]==1:
        t[y][x]=0
        
        for i in [-1,0,1]:
            d_y=y+i
            if d_y>=0 and d_y<h:
                for j in [-1,0,1]:
                    d_x=x+j
                    if d_x>=0 and d_x<w:
                        if t[d_y][d_x]==1:
                            dfs(d_x,d_y)
                    
for i in range(h):
    for j in range(w):
        if t[i][j]==1:               
            ans+=1
            dfs(j,i)
            
print(ans)