arr1 = [9,7,8,9,7,1,3,1,9,7,4,7]
arr2 = [9,4,5,1]
dic = {}

#Creating Dictionary
for i in arr1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i] = 1
print(dic)

#Removing non matching elements

for j in list(dic.keys()):
    if j in arr2:
        pass
    else:
        del(dic[j])
print(dic)

#Finding max appers element
max = 0
for k in list(dic.keys()):
    if dic[k] > max:
        max = dic[k]
        key = k
print(f"{key} appers {max} times")


