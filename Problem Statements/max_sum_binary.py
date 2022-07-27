# Given an array of T length each Index contain array of two
# binary strings,your task is to return their maximum sum
# (also a binary string).

# First Line contain T array length,
# Next n lines contain two string which shows binary space
# separated m,n

# find the sum of m and n in binary and print the maximum
# binary sum from the array elements

t = int(input("Enter Length of Array: "))
arr = []
for i in range(t):
    A,B = input().split()
    arr.append([A,B])

def max_sum(t,arr):
    max = 0
    for i in range(len(arr)):
        sum = int(arr[i][0],2) + int(arr[i][1],2)
        if sum > max:
            max = sum
    print(max)
    
max_sum(t,arr)