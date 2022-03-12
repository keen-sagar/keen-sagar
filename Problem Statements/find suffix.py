# find the  length of lexicographical smallest suffix string.
# Ex: string - qwtyeru , suffix from y is eru
str1 = "abcdecafgh"
query = "bc"

'''def lexi(str1,query):
    a = str1
    q = query
    ans = 0
    for i in q:
        k= a.find(i)
        if k == -1:
            ans+=0
        else:
            s=a[k:]
            ans+=s
    return (ans)

print(lexi(str1,query))'''
for i in query:
    k=str1.find(i)
    s=str1[k:]
print(s)
