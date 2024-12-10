import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

class BostonHousing:
    def __init__(self):
        self.model = None
        self.history = None
        self.x_train = None
        self.x_test = None
        self.y_train = None 
        self.y_test = None

    def prepare_data(self, test_split=0.2):
        # Load Boston Housing dataset
        (self.x_train, self.y_train), (self.x_test, self.y_test) = keras.datasets.boston_housing.load_data()
        
        # Normalize features
        mean = np.mean(self.x_train, axis=0)
        std = np.std(self.x_train, axis=0)
        self.x_train = (self.x_train - mean) / std
        self.x_test = (self.x_test - mean) / std
        
        return self.x_train, self.x_test, self.y_train, self.y_test

    def build_model(self):
        self.model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(self.x_train.shape[1],)),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(1)  # No activation for regression
        ])
        
        self.model.compile(
            optimizer='adam',
            loss='mse',  # Mean Squared Error
            metrics=['mae']  # Mean Absolute Error
        )
        
        return self.model

    def train(self, epochs=100, batch_size=32, validation_split=0.2):
        if self.model is None:
            self.build_model()
        
        if self.x_train is None:
            self.prepare_data()
        
        self.history = self.model.fit(
            self.x_train, 
            self.y_train, 
            epochs=epochs, 
            batch_size=batch_size, 
            validation_split=validation_split
        )
        
        return self.history

    def plot_loss(self):
        if self.history is None:
            print("Model not trained yet. Call train() first.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.history.history['loss'], label='Training Loss')
        plt.plot(self.history.history['val_loss'], label='Validation Loss')
        plt.title('Boston Housing Model Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Mean Squared Error')
        plt.legend()
        plt.show()

    def evaluate(self):
        if self.model is None or self.x_test is None:
            print("Model or test data not prepared. Call build_model() and prepare_data() first.")
            return
        
        test_loss, test_mae = self.model.evaluate(self.x_test, self.y_test)
        print(f"Test Loss (MSE): {test_loss:.4f}")
        print(f"Test MAE: {test_mae:.4f}")
        
        return test_loss, test_mae