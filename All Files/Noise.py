import numpy as np
from PIL import Image as im
import matplotlib.image as image
img=image.imread('Encrypted.jpg')
A = np.array(img)
print(A.shape)

for i in range(0,300):
    for j in range(0,300):
        for k in range(0,A.shape[2]):
            A[i][j][k] = 0

data = im.fromarray(A)
data.save('noise.png')