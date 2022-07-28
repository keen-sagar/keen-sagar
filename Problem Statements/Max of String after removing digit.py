#Remove digit d from string n only once and print the maximum value in string
n = "1231"
d = "1"
ans = []
for i in range(len(n)):
  if n[i] == d:
      ans.append(n[0:i] + n[i+1:])
print(max(ans))