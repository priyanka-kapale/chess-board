import numpy as np 
import matplotlib.pyplot as plt 
# LogNorm Normalize a given value to the 0-1 range on a log scale.
from matplotlib.colors import LogNorm  



# Declare the size of the interval dx, dy
dx, dy = 0.015, 0.05 
x = np.arange(-4.0, 4.0, dx) 
y = np.arange(-4.0, 4.0, dy) 
X, Y = np.meshgrid(x,y) 
min_max = np.min(x), np.max(x), np.min(y), np.max(y) 
res = np.add.outer(range(8), range(8))%2 
plt.imshow(res, cmap="binary_r")
plt.xticks([])
plt.yticks([])
plt.title("Chess Board Using Matplotlib Python") 
plt.show()