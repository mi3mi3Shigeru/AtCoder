m=int(input())
d=list(map(int,input().split()))

date=(sum(d)+1)//2
count=int(0)
for i in range(m):
    for j in range(d[i]):
        count+=1
        if date==count:
            print(str(i+1),str(j+1))
            break