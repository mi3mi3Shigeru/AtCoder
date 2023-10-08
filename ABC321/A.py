N=input()
digit_count = len(str(N))
is_like_Number=True

for i in range(digit_count-1):
    if int(N[i])<=int(N[i+1]):
        is_like_Number=False
        break
    
if is_like_Number:
    print("Yes")
else:
    print("No")