#Given a Triangle t, we have to find minimum sum path from top to bottom
t = [[2],[3,4],[6,5,7],[4,1,8,3]]
for i in range(len(t)-2,-1,-1):
    for j in range(len(t[i])):
        t[i][j] = min(t[i+1][j] + t[i][j], t[i+1][j+1] + t[i][j])
print("Minimum Path sum from top to bottom: ",t[0][0])