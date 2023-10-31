n=int(input())
ans="No"

while (n%2==0):
    n=n//2

while (n%3==0):
    n=n//3
if n==1:
    ans="Yes"
print(ans)
