import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

depth = 100
size = 4000

c_real = 0.2
c_imag = 0.6

shift = size/2
k = size/4

def check_is_in(x, y, cx, cy, n):
    if n == 0:
        return 0
    if x**2 + y**2 >= 4:
        return n
    else:
        x_ = x**2 - y**2 + cx
        y_ = 2*x*y + cy
        return check_is_in(x_, y_, cx, cy, n-1)

img = np.empty([size, size], dtype=np.int16)

for i in tqdm(range(size)):
    for j in range(size):
        img[i, j] = check_is_in((i-shift)/k, (j-shift)/k, c_real, c_imag, depth)

plt.imshow(img, cmap='hot', interpolation='bilinear')
plt.axis('off')
plt.show()