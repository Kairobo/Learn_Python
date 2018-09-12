import numpy, scipy.io
import numpy as np
arr = numpy.arange(9)
arr = arr.reshape((3, 3))  # 2d array of 3x3
arr = np.arange(10)
scipy.io.savemat('./arrdata.mat', mdict={'arr': arr})