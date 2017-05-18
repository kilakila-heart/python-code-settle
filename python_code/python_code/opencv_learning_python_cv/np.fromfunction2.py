import numpy as np
print np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
