arr = [5,3,2,1,4]
def inversion(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count+=1
    return count

result = inversion(arr)
print(f"There are {result} possibilities")