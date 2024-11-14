import numpy as np

class Errors:
    def cross_entroy_error(self, y, t):
        delta = 1e-7
        batch_size = 1 if y.ndim == 1 else y.shape[0]
        return np.sum(t*np.log(y + delta)) / batch_size