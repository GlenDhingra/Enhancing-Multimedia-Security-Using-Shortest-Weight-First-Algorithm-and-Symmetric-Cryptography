import random
arr = [100,200,300]
key1 = 5

def xor(mat):
    for i in range(0,len(mat)):
       mat[i] = mat[i] ^ key1
    

def nt(mat):
    for i in range(0,len(mat)):
        mat[i] = ~mat[i]

def leftShift(mat):
    temp = mat[0]
    for i in range(0,len(mat)-1):
        mat[i] = mat[i+1]
    mat[len(mat)-1] = temp


def rightShift(mat):
    temp = mat[len(mat)-1]
    for i in range(len(mat)-1,0,-1):
        mat[i] = mat[i-1]
    mat[0] = temp



mat = [
[0,4,0,0,0,0,0,8,0],
[4,0,8,0,0,0,0,11,0],
[0,8,0,7,0,0,0,0,2],
[0,0,7,0,9,14,0,0,0],
[0,0,0,9,0,10,0,0,0],
[0,0,4,14,10,0,2,0,0],
[0,0,0,0,0,2,0,1,6],
[8,11,0,0,0,0,1,0,7],
[0,0,2,0,0,0,6,7,0]
]

d = [0,999,999,999,999,999,999,999,999]
flag = [False,False,False,False,False,False,False,False,False]
root = [100,100,100,100,100,100,100,100,100]
u=0
count=1

def getMinIndex(arr):
    min = 99
    minIndex = 0
    for i in range(0,len(arr)):
        if(flag[i]==False and arr[i] > 0 and arr[i] < min):
            min = arr[i]
            minIndex = i
    return minIndex

while(count > 0):
    count = 0
    flag[u] = True
    
    vList = []
    for i in range(0,len(mat[u])):
        if(mat[u][i] != 0):
            vList.append(i)
    
    for i in range(0,len(vList)):
        temp = d[u] + mat[u][vList[i]]
        if(temp < d[vList[i]]):
            d[vList[i]] = temp
            root[vList[i]] = u

    u = getMinIndex(d)
    vList.clear()
    for i in range(0,len(flag)):
        if(flag[i] == False ):
            count = count + 1

for i in range(1,len(root)):
    print(i , root[i])
    pass

#creating random arr for assigning each node with functions
ops = []
for i in range(0,len(mat)):
    ops.append(random.randrange(1,5,1))


start = 0
end = 4
print(ops)
while(end != start):
    print(ops[end],end)
    if(ops[end] == 1):
        nt(arr)
        print("not")
    elif(ops[end] == 2):
        xor(arr)
        print("xor")
    elif(ops[end] == 3):
        leftShift(arr)
        print("ls")
    else:
        rightShift(arr)
        print("rs")
    end = root[end]
    print(arr)