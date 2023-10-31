k=int(input())
num=["0","1","2","3","4","5","6","7","8","9"]
a=["1","2","3","4","5","6","7","8","9"]
count=0
l=1
flag=True

def search(index,l,s):
    global a

    if index>0:
        search(index-1,l,s)
    s+=num[index]
    if l==0:
        a.append(s)
    elif l>0 and int(s[len(s)-1])>0:
        search(int(s[len(s)-1])-1,l-1,s)

while flag:
    for i in range(1,10):
        s=str(i)
        search(i-1,l-1,s)
        if len(a)>=k:
            flag=False
            break
    l+=1

print(a[k-1])