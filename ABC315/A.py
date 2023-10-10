s=input()
remove_word=["a","i","u","e","o"]
for word in remove_word:
    s=s.replace(word,"")
print(s)