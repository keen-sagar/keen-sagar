# list must be sorted to implement binary search
pos =0
def search(list,find):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2

        if list[mid] == find:
            globals()['pos']= mid+1
            return True
            break
        elif list[mid] > find:
            u = mid-1
        else:
            l = mid+1
    return False




list = [10,12,17,19,42,65]
find = 65


if search(list,find):
    print("Found at position",pos)
else:
    print("not found")
sorted()
