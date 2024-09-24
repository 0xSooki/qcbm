import numpy as np


def mmd_loss(sigma, X, Y):
    X = np.array(X)
    Y = np.array(Y)

    n, m = X.shape[0], Y.shape[0]

    if n == 0 or m == 0:
        return 0.

    XX = np.sum([k(sigma, x, xx) for x in X for xx in X]) / (n ** 2)
    YY = np.sum([k(sigma, y, yy) for y in Y for yy in Y]) / (m ** 2)
    XY = np.sum([k(sigma, x, y) for x in X for y in Y]) / (n * m)

    mmd_squared = XX + YY - 2 * XY

    return np.sqrt(mmd_squared)


# gaussian kernel
def k(sigma, x, y):
    return np.exp(-np.linalg.norm(x - y) ** 2 / (2 * sigma ** 2))
