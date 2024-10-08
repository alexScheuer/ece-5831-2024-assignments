
import numpy as np
import matplotlib.pyplot as plt

class MultilayerPerceptron:
    def __init__(self):
        pass
    
    # Step function - numpy version
    def step_function(self, x):
        return (x > 0).astype(int)
    
    # Sigmoid function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    # Plot step function
    def plot_step_function(self):
        x = np.arange(-10.0, 10.0, 0.1)
        y = self.step_function(x)
        plt.plot(x, y)
        plt.title('Step Function')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.show()
    
    # Plot sigmoid function
    def plot_sigmoid_function(self):
        x = np.arange(-10.0, 10.0, 0.1)
        y = self.sigmoid(x)
        plt.plot(x, y)
        plt.title('Sigmoid Function')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.show()
