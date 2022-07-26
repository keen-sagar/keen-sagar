N = 10               # no. of days
M = 5               # no. of obligations 
K = 2               # no. of obligations cancelled 
D = [2,3,6,7,9]           # days of obligation

def max_vacation(n,m,k,d):
    d.sort()
    max = 0
    start = 1
    for i in range(m-k):
        end = d[k+i]
        days = end - start
        start = d[i]+1
        if days > max:
            max = days
    end = n+1
    if (end - start) > max:
            max = end - start
    return max
    
    
result = max_vacation(N,M,K,D)
print(f"Max Holidays he can get is: {result} Days")
