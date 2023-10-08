n,m= map(int, input().split())
s=input()
t=input()
is_prefix=False
is_suffix=False
answer=3

if t.startswith(s):
    is_prefix=True

if t.endswith(s):
    is_suffix=True

    
if is_prefix:
    if is_suffix:
        answer=0
    else:
        answer=1
else:
    if is_suffix:
        answer=2
    else:
        answer=3

print(str(answer))

# n,m= map(int, input().split())
# s=input()
# t=input()
# is_prefix=False
# is_suffix=False
# answer=3

# if str(s) in str(t[0:n]):
#     is_prefix=True

# if str(s) in str(t[m-n:m]):
#     is_suffix=True

# if is_prefix:
#     if is_suffix:
#         answer=0
#     else:
#         answer=1
# else:
#     if is_suffix:
#         answer=2
#     else:
#         answer=3

# print(str(answer))