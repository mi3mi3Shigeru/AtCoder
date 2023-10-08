n,x= map(int, input().split())
a = list(map(int,input().split()))

max_score=int(max(a))
min_score=int(min(a))
total=sum(a)

total-=(max_score+min_score)
answer=int(x-total)

#ここの=をつけ忘れてました。泣きそうです。
if min_score>=answer:
    answer=0

if answer>max_score:
    answer=-1

print(str(answer))