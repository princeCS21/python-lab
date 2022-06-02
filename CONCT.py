#ARRAY CONCATINATION
import numpy as np  
a = np.array([[21,52,30],[10,15,14]])  
b = np.array([[12,62,37],[12, 29, 29]])  
print("vertically concatenated\n",np.vstack((a,b)))  
print("horizontally concatenated\n",np.hstack((a,b)))  
