import numpy as np
from PIL import Image as im

import matplotlib.image as image
img=image.imread('starfish.jpg')
print(img.shape)
print("-------------")
A = np.array(img)



mat = np.random.rand(int((img.shape[0]))+1,int((img.shape[0]))+1)
# mat = np.array([
#     [2,10,30,50,70,5],
#     [10,3,30,25,100,50],
#     [54,45,4,100,10,20],
#     [100,90,50,5,10,40],
#     [5,10,20,50,4,40],
#     [15,20,30,50,40,2]
# ])
print(mat.shape)

X=[]
for i in range(0,mat.shape[0]):
    X.append(np.array([]))

# X1 = np.array([])
# X2 = np.array([])
# X3 = np.array([])
# X4 = np.array([])
# X5 = np.array([])
# X6 = np.array([])
# X7 = np.array([])
# X8 = np.array([])
# X9 = np.array([])
# X10 = np.array([])

# X = [X1,X2,X3,X4,X5,X6,X7,X8,X9,X10]


blockSize = int(1800 / (mat.shape[0]-1))
print(blockSize)
start_p = 0
end_p = blockSize

#flag = [True,False,False,False,False,False,False,False,False,False]
flag1 = np.array([0])


visited = 1
count = mat.shape[0]
min_index = 0
while(visited < count):
    arr = mat[min_index]
    min = 1000
    """and flag[i] == False"""
    for i in range(0,len(arr)):
        if( i != min_index  and arr[i] < min and (i not in flag1) ):
            min = arr[i]
            min_index = i
    #print(min_index)
    X[min_index] = A[start_p:end_p]
    print('------------',start_p,end_p)
    #print(X[min_index])
    start_p = start_p + blockSize
    end_p = end_p + blockSize
    #flag[min_index] = True
    flag1 = np.append(flag1,min_index)
    visited = visited + 1

print(flag1)
#merge_arr = np.concatenate([X[1],X[2],X[3],X[4],X[5],X[6],X[7],X[8],X[9]],axis=0)
merge_arr = np.concatenate(X[1:],axis=0)
print(merge_arr.shape)

data = im.fromarray(merge_arr)
data.save('Encrypted.png')
print("Image formed")




# X1, X2, X3, X4, X5, X6 = np.split(test, 6, axis=0) #Array, num of splits, axis for splitting
# X = [X1,X2,X3,X4,X5,X6]


