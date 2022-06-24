arr1 = [11,2,4,6,10]
arr2 = [3,5,7,8]
def sortarr(arr1,arr2):
    arr1 = list(set(arr1+arr2))
    l = len(arr1) - len(arr2)
    for i in range(len(arr2)):
        arr2[i] = arr1[l]
        del(arr1[l])
    return arr1,arr2


arr1,arr2 = sortarr(arr1,arr2)
print(arr1)
print(arr2)
