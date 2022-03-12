from array import *
x = int(input("Enter the size if an array "))                   # taking size of array
marks = array('i',[])                                           # initialising empty array
for i in range(x):                                              # creating range till size x
    print("Enter ",i+1," value ",end="")
    n=int(input(""))                                            # taking value of array from user
    marks.append(n)                                             # adding value to array

print(marks)

find = int(input("Enter the number to find its index number "))
print(marks.index(find))                                        # in-built function to find index of number

k=0                                                             # user-built loop to find index of number
for i in marks:
    if(find == i):
        print(k)
        break
    k+=1

