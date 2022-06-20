arr = [[1,3],[2,6],[8,10],[8,9],[9,11],[15,18],[2,4],[16,17]]
arr.sort()
print(arr)

arr2 = []
for k in range(1,len(arr)):
    for i in range(1,len(arr)):
        if arr[i][0] <= arr[i-1][1]:
            arr[i-1][1] = max(arr[i][1],arr[i-1][1])
            arr2.append(i)
arr2 = list(set(arr2))
for j in arr2[::-1]:
    del(arr[j])


print(arr)