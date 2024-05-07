import numpy  # 1

arr =numpy.array([1, 2, 3, 4, 5])

print(arr)


import numpy as np  # 2

print(np.__version__)

a=np.array([1,25,23.2,44])  # 3

print(type(a))

b=np.array([1,25,23.2,44,"ani"])  #4

print(b)

#### dimension in array

# "0  dimension"

c=np.array(5862)

print(c)


# " 1  dimension" , "2 dimension ", "3  dimension"

d=np.array([[1,8,3],[2,5,8],[5,8,9]])

print(d[0,1])

print(d[1,2])

print(d[2,0])

print(d[1,1]+d[2,2])



