import numpy as np
import mnist
from activations import Activations
from errors import Errors
from collections import OrderedDict
from layers import Affline
from layers import Relu
from layers import SoftmaxWithLoss

class TwoLayerNetWithBackProp:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # Initialize weights and biases
        self.params = {}
        self.params['w1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['w2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        self.activation = Activations()
        self.errors = Errors()

        #Additional layers
        self.layers = OrderedDict()
        self.layers['Affline1'] = Affline(self.params['s1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affline2'] = Affline(self.params['s2'], self.params['b2'])
        self.last_layer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values[]:
            x = layer.forward(x)
        y = x
        return y

    def loss(self, x, y):
        y_hat = self.predict(x)
        #return self.errors.cross_entropy_error(y_pred, y_true)
        return self.last_layer.forward(y_hat, y)

    def accuracy(self, x, y):
        y_hat = self.predict(x)
        p = np.argmax(y_hat, axis=1)
        y_p = np.argmax(y, axis=1)

        return np.sum(p == y_p) / float(x.shape[0])

    #multi-dimensional
    def _numerical_gradient(self, f, x):
        h = 1e-4
        grad = np.zeros_like(x)

        it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            idx = it.multi_index
            tmp_val = x[idx]
            x[idx] = float(tmp_val) + h
            fxh1 = f(x)  # f(x+h)
            x[idx] = tmp_val - h
            fxh2 = f(x)  # f(x-h)
            grad[idx] = (fxh1 - fxh2) / (2 * h)
            x[idx] = tmp_val  # Restore value
            it.iternext()

        return grad

    def numerical_gradient(self, x, y_true):
        loss_fn = lambda w: self.loss(x, y_true)

        grads = {}
        grads['w1'] = self._numerical_gradient(loss_fn, self.params['w1'])
        grads['b1'] = self._numerical_gradient(loss_fn, self.params['b1'])
        grads['w2'] = self._numerical_gradient(loss_fn, self.params['w2'])
        grads['b2'] = self._numerical_gradient(loss_fn, self.params['b2'])

        return grads

    def gradient(self, x, y):
        self.loss(x, y)
        dout = 1
        dout = self.last_layer.backward(dout)
        layers = list(self.layers.values())
        layers_reverse()
        for layer in layers:
            dout = layer.backward(dout)

        grads = {}
        grads['w1'] = self.layers['Affline1'].dx
        grads['b1'] = self.layers['Affline1']
        grads['w2'] = self.layers['Affline2']
        grads['b2'] = self.layers['Affline2']
        return grads
