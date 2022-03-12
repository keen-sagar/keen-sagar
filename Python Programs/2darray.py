from numpy import *


"""arr = array([1,2,3,4,5,6])
arr1 = arr.view()                   # copying is of 3 types 
arr1[0] = 0                         # arr1 = arr---- will have two connected array with same address 
print(arr)                          # arr1 = arr.copy() ---- will have two connected array with different address
print(id(arr))                      # arr1 = arr.view() ---- will have two independent array
print(arr1)
print(id(arr1))"""

"""arr = array([[2,3,4],[1,3,4],[4,5,6]])
print(arr.flatten())                        #  convert 2d to 1d array
print(arr.reshape(3,3))"""                     # will reshape array to 1d,2d,3d ad per given parameters

m = matrix('3 4;4 5')                       # creating a matirx, can be crated with existing array ---- matrix(arr)
print(m)