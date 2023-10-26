import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image

# read image
im=image.imread('Encrypted.jpg')
#im=image.imread('Encrypted.jpg')
#im=image.imread('Decrypted.jpg')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# calculate histogram
counts, bins = np.histogram(vals, range(257))
# plot histogram centered on values 0..255
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()