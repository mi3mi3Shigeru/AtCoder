import math

N=input()
n=N.split(" ")
a=int(n[0])
b=int(n[1])

answer=int(math.pow(a,b)+math.pow(b,a))
print(str(answer))