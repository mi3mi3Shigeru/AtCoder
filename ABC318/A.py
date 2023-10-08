S=input()
s=S.split(" ")
N=int(s[0])
M=int(s[1])
P=int(s[2])

if N-M>=0:
    answer= 1+((N-M)//P)
else:
    answer=0
print(str(answer))