import numpy as np
from PIL import Image as im

import matplotlib.image as image
from numpy.matrixlib.defmatrix import mat
from collections import deque

img=image.imread('test_1.jpg')
print(img.shape)

unique = np.unique(sorted(img.flatten()))
unique = unique[0:51]

#Equation
def a(x,y):
    return (2*x)+(3*y)

def b(x,y):
    return abs((x**2)-(y**2))

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



unique = unique[0:451]

# def leftRotate(a, d):
#     b = []
#     for i in range(-d,len(a)):
#         b.append(a[i])
#     b.extend(a[0:d])
#     return b

def leftShift(mat):
    temp = mat[0]
    for i in range(0,len(mat)-1):
        mat[i] = mat[i+1]
    mat[len(mat)-1] = temp
    return mat

def rightRotate(lists, num):
    output_list = []
 
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
    for item in range(0, len(lists) - num):
        output_list.append(lists[item]) 
    return output_list

matrix = np.array([unique])
#mat = np.array([1,2,3,4,5])
for i in range(1,len(unique)):
    # matrix = np.vstack([matrix,rightRotate(matrix[i-1],i)])
    # matrix = np.vstack([matrix,leftShift(matrix[i-1])])
    temp = deque(unique)
    if( i % 2 == 0):
        temp.rotate(c(i))
        #print("Here")
        matrix = np.vstack([matrix,temp])
    else:
        temp.rotate(-c(i))
        #print("There")
        matrix = np.vstack([matrix,temp])

print(matrix.shape)
