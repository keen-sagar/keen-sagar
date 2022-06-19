def sortarr(arr):
    for j in range(len(arr)-1):
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]

    return arr

arr = [1,2,2,1,1,2,0]
print(sortarr(arr))