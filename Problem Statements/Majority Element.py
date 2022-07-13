arr = [1,2,2,1,1,1,2,2,3,1,1]


# Using optimal Approach
def me(arr):
    ele = arr[0]
    count = 1
    for i in range(1,len(arr)):
        if arr[i] == ele:
            count += 1
        elif count > 0:
            count -= 1
        else:
            ele = arr[i]
            count = 1
    print(f"Majority Element is :{ele}")


# Using Dictionary(key,value)pair
def me2(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    for j in dict:
        if dict[j] > len(arr)/2:
            print(f"Majority Element is :{j}")


me2(arr)
