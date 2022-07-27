n = 6
arr = [0]*(n+1)
arr[0],arr[1] = 0,1

for i in range(1,(n//2)+1):
    arr[2*i] = arr[i]
    if arr[n] == 0:
        arr[(2*i)+1] = arr[i] + arr[i+1]
    else:
        break
print(arr)
print(f"Maximum element: {max(arr)}")