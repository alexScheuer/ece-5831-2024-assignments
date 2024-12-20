from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, AveragePooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model


class LeNet:
    def __init__(self, batch_size=32, epochs=20):
        self.batch_size = batch_size
        self.epochs = epochs
        self.model = None
        self.x_test = None
        self.y_test = None
        self._create_lenet()
        self.compile()

    def _create_lenet(self):
        self.model = Sequential([
            Conv2D(filters=6, kernel_size=(5,5), activation='sigmoid', input_shape=(28, 28, 1), padding='same'),
            AveragePooling2D(pool_size=(2, 2), strides=2),

            Conv2D(filters=6, kernel_size=(5,5), activation='sigmoid', padding='same'),
            AveragePooling2D(pool_size=(2, 2), strides=2),

            Flatten(),

            Dense(120, activation='sigmoid'),
            Dense(84,  activation='sigmoid'),
            Dense(10,  activation='softmax')
        ])

    def compile(self):
        if self.model is None:
            print('Error: Create model first!')

        self.model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def preprocess(self):
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        #normalize
        x_train = x_train/255.0
        x_test = x_test/255.0

        #one-hot encoding
        self.y_train = to_categorical(y_train, 10)
        self.y_test = to_categorical(y_test, 10)

        #add channel dim
        self.x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
        self.x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)


    def train(self):
        self.preprocess()
        self.compile()
        self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.epochs)

    def save(self, model_path_name):
        # Save the model with the specified file name
        self.model.save(f"{model_path_name}.keras")

    def load(self, model_path_name):
        # Load the model with the specified file name
        self.model = load_model(f"{model_path_name}.keras")

    def predict(self, images):
        images = images.reshape((-1, 28, 28, 1)) 

        predictions = self.model.predict(images)

        return predictions.argmax(axis=1)
