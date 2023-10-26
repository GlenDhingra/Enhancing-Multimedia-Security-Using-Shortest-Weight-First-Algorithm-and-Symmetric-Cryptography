import numpy as np
mat = np.array([[[10,20,30],[20,30,40],[30,40,50]],
                [[10,20,30],[20,30,40],[30,40,50]]
])

for i in mat:
    for j in i:
        print(j)
print(mat.shape)

#key1 = 5
# def xor(mat):
#     for i in range(0,len(mat)):
#        mat[i] = mat[i] ^ key1
    

# def nt(mat):
#     for i in range(0,len(mat)):
#         mat[i] = ~mat[i]

# def leftShift(mat):
#     temp = mat[0]
#     for i in range(0,len(mat)-1):
#         mat[i] = mat[i+1]
#     mat[len(mat)-1] = temp


# def rightShift(mat):
#     temp = mat[len(mat)-1]
#     for i in range(len(mat)-1,0,-1):
#         mat[i] = mat[i-1]
#     mat[0] = temp


# xor(mat)
# print(mat)
# nt(mat)
# print(mat)
# nt(mat)
# print(mat)
# leftShift(mat)
# print(mat)
# rightShift(mat)
# print(mat)