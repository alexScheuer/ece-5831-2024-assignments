import numpy as np
import pickle
from mnist import load_mnist
from TwoLayerNetWithBackProp import TwoLayerNetWithBackProp

(x_train, y_train), (x_test, y_test) = load_mnist(normalize=True, one_hot_label=True)

iterations = 10000
batch_size = 16
learning_rate = 0.01

# Initialize the network
input_size = 784  # 28x28
hidden_size = 50
output_size = 10
network = TwoLayerNetWithBackProp(input_size, hidden_size, output_size)

# Training loop
train_size = x_train.shape[0]
for i in range(iterations):
    batch_indices = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_indices]
    y_batch = y_train[batch_indices]

    grads = network.gradient(x_batch, y_batch)

    for key in ('w1', 'b1', 'w2', 'b2'):
        network.params[key] -= learning_rate * grads[key]

    if i % 1000 == 0:
        loss = network.loss(x_batch, y_batch)
        print(f"Iteration {i}, Loss: {loss}")

# Save the trained model to a pickle file
model_filename = 'scheuer_mnist_model.pkl'
with open(model_filename, 'wb') as f:
    pickle.dump(network.params, f)
