# Imports
import numpy as np
from PIL import Image as im
import matplotlib.image as image
from collections import deque
import matplotlib.pyplot as plt
import sys
import time
begin = time.time()
# Reading and converting img to matrix
img=image.imread('painting.jpg')
A = np.array(img)
print(A.shape[0])
# Fetching 50 unique sorted values from matrix
unique = np.unique(sorted(img.flatten()))
unique = unique[0:51]

#####

####

# Key 1
def a(x,y):
    return (2*x)+(3*y)

# Key 2
def b(x,y):
    return abs((x**2)+(y**2))

# key 3
def c(x):
    return ( (3 * (x**4)) - (7 * (x**3)) - (12 * (x**2)) )


# Generating values using Key 1
for i in range(0,len(unique)-1):
    x = unique[i]
    y = unique[i+1]
    unique = np.append(unique,a(x,y))
    x,y = y,x
    unique = np.append(unique,a(x,y))

# Generating values using Key 2
for i in range(0,len(unique)-1):
    x = unique[i]
    y = unique[i+1]
    unique = np.append(unique,b(x,y))
    x,y = y,x
    unique = np.append(unique,b(x,y))

# Slicing unique_array values to make them divisible by image matrix for node generation
unique = unique[0:int(img.shape[0]/4)+1]

# Creating matrix for greedy algorithm by left/right shifting unique_array elements using Key 3
matrix = np.array([unique])
for i in range(1,len(unique)):
    temp = deque(unique)
    if( i % 2 == 0):
        temp.rotate(c(i))
        matrix = np.vstack([matrix,temp])
    else:
        temp.rotate(-c(i))
        matrix = np.vstack([matrix,temp])

# Creating nodes for Greedy Algorithm
X=[]
for i in range(0,matrix.shape[0]):
    X.append(np.array([]))

blockSize = int(1800 / (matrix.shape[0]-1)) # To determine number of rows in each node
start_pointer = 0         # Starting pointer to rows to be added in each node
end_pointer = blockSize   # End pointer to rows to be added in each node

flag = np.array([0])   # Flag to mark visited nodes in Greedy Algorithm

visited = 1        # Count number of nodes visited for terminating while loop [Set to 1 as starting Node will not carry data]
count = matrix.shape[0]    # For terminating while loop
min_index = 0           # To start greedy algorithm from 0th node

xor_pointer = 1

#Greedy Algorithm along with OUR algorithm
while(visited < count):
    arr = matrix[min_index]
    min = sys.maxsize
    for i in range(0,len(arr)):
        if( i != min_index  and arr[i] < min and (i not in flag) ):
            min = arr[i]
            min_index = i
    X[min_index] = A[start_pointer:end_pointer]
    X[min_index] = X[min_index] ^ (xor_pointer % 255)
    xor_pointer = xor_pointer + min_index
    start_pointer = start_pointer + blockSize       
    end_pointer = end_pointer + blockSize
    flag = np.append(flag,min_index)
    visited = visited + 1

merge_arr = np.concatenate(X[1:],axis=0)        # Merging values in all nodes in ascending order of nodes to get shuffled matrix
#merge_arr = ~merge_arr      # Performing NOT operation to change colour of image
end = time.time()
print(f"Total runtime of the program is {end - begin}")
data = im.fromarray(merge_arr)
data.save('Encrypted.jpg')
data.save('Encrypted.png')  #Save encrypted image
print("Image formed")