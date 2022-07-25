A = [10,2,3,4,50]
x = 1
y = 2

def low_cost(A,x,y):
    cost = 0
    while (len(A) > 0):
        if (max(A)*x) >= (len(A)*y):
            i = A.index(max(A))
            cost = cost + y
            del(A[i])
        else:
            cost = cost + (max(A)*x)
            A = []
    print(f"The Cost of Whole Operation is: {cost}")


low_cost(A,x,y)
