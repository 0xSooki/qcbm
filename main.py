import circuit as circ
import numpy as np
arr = np.array([[0,1,0, 0,0], [0,1,1, 0, 1], [1,1,1, 1, 1]])
circ.create_circ(5, arr)