import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

class Reuters:
    def __init__(self):
        self.model = None
        self.history = None
        self.x_train = None
        self.x_test = None
        self.y_train = None 
        self.y_test = None

    def prepare_data(self, max_words=10000, num_classes=46):
        # Load Reuters dataset
        (self.x_train, self.y_train), (self.x_test, self.y_test) = keras.datasets.reuters.load_data(num_words=max_words, test_split=0.2)
        
        # One-hot encode labels
        self.y_train = keras.utils.to_categorical(self.y_train, num_classes)
        self.y_test = keras.utils.to_categorical(self.y_test, num_classes)
        
        # Pad sequences
        self.x_train = keras.preprocessing.sequence.pad_sequences(self.x_train)
        self.x_test = keras.preprocessing.sequence.pad_sequences(self.x_test, maxlen=self.x_train.shape[1])
        
        return self.x_train, self.x_test, self.y_train, self.y_test

    def build_model(self, max_words=10000, num_classes=46):
        self.model = keras.Sequential([
            keras.layers.Embedding(max_words, 16, input_length=self.x_train.shape[1]),
            keras.layers.GlobalAveragePooling1D(),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(num_classes, activation='softmax')
        ])
        
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return self.model

    def train(self, epochs=20, batch_size=128, validation_split=0.2):
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
        plt.title('Reuters Model Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

    def plot_accuracy(self):
        if self.history is None:
            print("Model not trained yet. Call train() first.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.history.history['accuracy'], label='Training Accuracy')
        plt.plot(self.history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Reuters Model Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.show()

    def evaluate(self):
        if self.model is None or self.x_test is None:
            print("Model or test data not prepared. Call build_model() and prepare_data() first.")
            return
        
        test_loss, test_accuracy = self.model.evaluate(self.x_test, self.y_test)
        print(f"Test Loss: {test_loss:.4f}")
        print(f"Test Accuracy: {test_accuracy:.4f}")
        
        return test_loss, test_accuracy