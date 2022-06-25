arr = [7,9,1,2,3,3,4,5,8]

def dup(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1

    for j in dic:
        if dic[j] > 1:
            print(f"{j} is a Duplicate Element")
    missing(dic)

def missing(dic):
    dic = list(set(dic))
    for i in range(1,len(dic)+1):
        if i not in dic:
            print(f"{i} is missing Element")




dup(arr)

