from numpy import *

# Insert an array in original array -
arr = array([12, 14, 15, 16, 17])
new_arr = array([18, 30, 56, 78, 23])

arr = insert(arr, 1, new_arr, axis=0)
print(arr)

# Apppend an array in original array - 
arr = array([12, 14, 15, 16, 17])
new_arr = array([18, 30, 56, 78, 23])

arr=new_arr[:,newaxis]

arr = append(arr, new_arr[:,newaxis],axis=1)
print(arr)
