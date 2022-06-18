def maxsum(arr):
    max = 0
    for k in range(1,len(arr)+1):
        for i in range(len(arr)+1-k):
            x = i+k
            if x > len(arr):
                x = len(arr)
            a = arr[i:x]
            sum = 0
            for j in a:
                sum = sum + int(j)
            if sum > max:
                max = sum
                subarr = a

    return max,subarr



arr = [-2,1,-3,4,-1,2,1,-5,4]
result,sub = maxsum(arr)
print(sub)
print(result)