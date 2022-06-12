def pascal(size):
    arr1 = [1]
    arr2 = []
    for i in range(size):
        for j in range(i+1):
            if j == 0:
                val = arr1[j]
            elif j == i:
                val = arr1[j-1]
            else:
                val = arr1[j] + arr1[j-1]
            arr2.append(val)
        show(size,arr2)
        arr1 = arr2
        arr2 = []
        size-=1


def show(size,arr2):
    #space = (size*2)-1
    for s in range(size-1):
        print(" ", end=" ")
    for l in range(len(arr2)):
        print(arr2[l],end=" ")
        print(" ",end=" ")
    print("")


size = int(input("Enter the Size: "))
pascal(size)