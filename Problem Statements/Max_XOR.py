from itertools import combinations


def fun(arr, N):
   sub = []
   max_xor = max(arr)
   for i in range(1, N // 2):
       comb = combinations(arr, i + 1)
       for i in comb:
           sub.append(list(i))
   for a in sub:
       z = 0
       for b in a:
           z = z ^ b
       if z > max_xor:
           max_xor = z
   return max_xor


N = int(input("Enter Length : "))
arr = []
for i in range(N):
   arr.append(int(input(f"Enter {i+1} Element : ")))
if N < 3:
   print("Output :", max(arr))
else:
   print("Output :", fun(arr, N))