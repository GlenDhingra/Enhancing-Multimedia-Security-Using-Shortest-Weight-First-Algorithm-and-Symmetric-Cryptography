import numpy as np
from PIL import Image as im

import matplotlib.image as image
img=image.imread('test_1.jpg')
#print(img.shape)
print("-------------")
A = np.array(img)
#print(A)
from collections import deque
#print(img.shape)

unique = np.unique(sorted(img.flatten()))
unique = unique[0:51]

#Equation
def a(x,y):
    return (2*x)+(3*y)

def b(x,y):
    return abs((x**2)+(y**2))

def c(x):
    return ( (3 * (x**4)) - (7 * (x**3)) - (12 * (x**2)) )

f_array = []

for i in range(0,len(unique)-1):
    x = unique[i]
    y = unique[i+1]

    unique = np.append(unique,a(x,y))
    x,y = y,x
    unique = np.append(unique,a(x,y))

for i in range(0,len(unique)-1):
    x = unique[i]
    y = unique[i+1]

    unique = np.append(unique,b(x,y))
    x,y = y,x
    unique = np.append(unique,b(x,y))



unique = unique[0:int(img.shape[0]/4)+1]

matrix = np.array([unique])
for i in range(1,len(unique)):
    temp = deque(unique)
    if( i % 2 == 0):
        temp.rotate(c(i))
        matrix = np.vstack([matrix,temp])
    else:
        temp.rotate(-c(i))
        matrix = np.vstack([matrix,temp])

#print(matrix.shape)
mat = matrix
#print(mat.shape)

X=[]
for i in range(0,mat.shape[0]):
    X.append(np.array([]))

blockSize = int(1800 / (mat.shape[0]-1))
#print(blockSize)
start_p = 0
end_p = blockSize
min_cost = 0

flag1 = np.array([0])

visited = 1
count = mat.shape[0]
min_index = 0
while(visited < count):
    arr = mat[min_index]
    min = 1000
    for i in range(0,len(arr)):
        if( i != min_index  and arr[i] < min and (i not in flag1) ):
            min = arr[i]
            min_cost = min
            min_index = i
    X[min_index] = A[start_p:end_p]
    start_p = start_p + blockSize
    end_p = end_p + blockSize
    flag1 = np.append(flag1,min_index)
    visited = visited + 1

#print(flag1)
merge_arr = np.concatenate(X[1:],axis=0)
#print(merge_arr.shape)
# merge_arr = merge_arr.flatten()
# for i in range(0,merge_arr.shape[0]):
#     merge_arr[i] = merge_arr[i] ^ (i*200)
# merge_arr =  merge_arr.reshape(1800,1800,3)
merge_arr = ~merge_arr

data = im.fromarray(merge_arr)
data.save('Encrypted.jpg')
print("Image formed")
#print(merge_arr)
unique = np.unique(merge_arr)
#print(len(unique))

#############################################################################
# Decrypt
#############################################################################

A=image.imread('Encrypted.jpg')
A = ~A
# A = A.flatten()
# for i in range(0,A.shape[0]):
#     A[i] = A[i] ^ (i*200)
# A =  A.reshape(1800,1800,3)


unique = np.unique(sorted(A.flatten()))
unique = unique[0:51]

#Equation
def a(x,y):
    return (2*x)+(3*y)

def b(x,y):
    return abs((x**2)+(y**2))

def c(x):
    return ( (3 * (x**4)) - (7 * (x**3)) - (12 * (x**2)) )


for i in range(0,len(unique)-1):
    x = unique[i]
    y = unique[i+1]

    unique = np.append(unique,a(x,y))
    x,y = y,x
    unique = np.append(unique,a(x,y))

for i in range(0,len(unique)-1):
    x = unique[i]
    y = unique[i+1]

    unique = np.append(unique,b(x,y))
    x,y = y,x
    unique = np.append(unique,b(x,y))


unique = unique[0:451]

matrix = np.array([unique])
for i in range(1,len(unique)):
    temp = deque(unique)
    if( i % 2 == 0):
        temp.rotate(c(i))
        matrix = np.vstack([matrix,temp])
    else:
        temp.rotate(-c(i))
        matrix = np.vstack([matrix,temp])

#print(matrix.shape)

mat = matrix

X=[]
for i in range(1,mat.shape[0]):
    X.append(np.array([]))

blockSize = int(1800 / (mat.shape[0]-1))
#print(blockSize)
start_p = 0
end_p = blockSize

flag1 = np.array([0])

visited = 1
count = mat.shape[0]
min_index = 0

pointer = 0

while(visited < count):
    arr = mat[min_index]
    min = 1000
    for i in range(0,len(arr)):
        if( i != min_index  and arr[i] < min and (i not in flag1) ):
            min = arr[i]
            min_index = i
    end_p = min_index * int( A.shape[0] / (mat.shape[0]-1) )     
    start_p = end_p - blockSize
    X[pointer] = A[start_p:end_p]
    flag1 = np.append(flag1,min_index)
    visited = visited + 1
    pointer = pointer + 1

merge_arr = np.concatenate(X[0:],axis=0)

merge_arr =  merge_arr.reshape(1800,1800,3)
#print(merge_arr.shape)
#print(merge_arr)
data = im.fromarray(merge_arr)
data.save('Decrypted.jpg')
#print("Image formed")
