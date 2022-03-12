def digitalsum(L):
    sum = 0
    for i in str(L):
        sum += int(i)
    if sum > 9:
        sum = digitalsum(sum)
    return sum

def main(Q,L,R,X):
    num = 0
    arr = []
    while num < Q:
        count = 0
        start = L[num]
        end = R[num]
        for i in range(start,end+1):
            if digitalsum(i) == X[num]:
                count += 1
        arr.append(count)
        num+=1
    xor = 0
    for i in range(Q):
        xor = xor ^ arr[i]
    return arr, xor



Q = 2
L = [1,1]
R = [100,19]
X = [1,2]

arr, xor = (main(Q,L,R,X))
print(arr)
print(xor)


