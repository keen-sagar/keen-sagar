# from array import *----- will import all method of array module and don't have to use method name when using
# from array import array----- will import array method of array module """"""""""saves memory
# import array as arr ----- will also import whole array module and have to use arr before using any method
# eg: marks = arr.array('H',[65,34,45,56])

from array import *
marks = array('H',[65,34,45,56])
a = marks
print(marks)            # print whole array

for i in marks:        # will print values 1 by 1----- or can use range(len(marks)) instead of marks
    print(i)

print(a)



arr = array('i',[2,3,4,5,6])            # in numpy we don't have to specify data type
print(arr)

arr1 = array('i',[])                    # 1 way to copy an array
for i in arr:
    arr1.append(i+5)
print(arr1)

arr2 = array(arr.typecode,[a+5 for a in arr])   # way 2 to copy an array
print(sum(arr))
