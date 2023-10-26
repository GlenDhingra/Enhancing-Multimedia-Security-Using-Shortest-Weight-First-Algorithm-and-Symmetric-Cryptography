import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im
import matplotlib.image as image

enc=image.imread('RSA-key-1.png')
dec = image.imread('RSA-key-2.png')

recover = np.subtract(enc,dec)

data = im.fromarray(recover)
data.save('Subtraction_after_key_change_rsa.png') 