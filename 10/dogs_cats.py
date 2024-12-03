import pathlib
import os
import shutil
import tensorflow as tf
import matplotlib.pyplot as plt

# Dataset and hyperparameters
CLASS_NAMES = ['dog', 'cat']
IMAGE_SHAPE = (180, 180, 3)
BATCH_SIZE = 32
BASE_DIR = pathlib.Path('dogs-vs-cats')
SRC_DIR = pathlib.Path('dogs-vs-cats-original/train')
EPOCHS = 20

class DogsCats:
    def __init__(self):
        self.train_dataset = None
        self.valid_dataset = None
        self.test_dataset  = None
        self.model         = None

    def make_dataset_folders(self, subset_name, start_index, end_index):
        for category in CLASS_NAMES:
            dir = BASE_DIR / subset_name / category
            if not os.path.exists(dir):
                os.makedirs(dir)
            files = [f'{category}.{i}.jpg' for i in range(start_index, end_index)]
            for file in files:
                shutil.copyfile(src=SRC_DIR / file, dst=dir / file)

    def _make_dataset(self, subset_name):
        return tf.keras.utils.image_dataset_from_directory(
            BASE_DIR / subset_name,
            image_size=IMAGE_SHAPE[:2],
            batch_size=BATCH_SIZE
        )

    def make_dataset(self):
        self.train_dataset = self._make_dataset('train')
        self.valid_dataset = self._make_dataset('validation')
        self.test_dataset  = self._make_dataset('test')

    def build_network(self, augmentation=True):
        inputs = tf.keras.layers.Input(shape=IMAGE_SHAPE)
        x = tf.keras.layers.Rescaling(1. / 255)(inputs)
        if augmentation:
            x = tf.keras.layers.RandomFlip("horizontal")(x)
            x = tf.keras.layers.RandomRotation(0.1)(x)
        x = tf.keras.layers.Conv2D(filters=16, kernel_size=3, activation="relu")(x)
        x = tf.keras.layers.AveragePooling2D(pool_size=2)(x)
        x = tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation="relu")(x)
        x = tf.keras.layers.AveragePooling2D(pool_size=2)(x)
        x = tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation="relu")(x)
        x = tf.keras.layers.AveragePooling2D(pool_size=2)(x)
        x = tf.keras.layers.Flatten()(x)
        outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
        self.model = tf.keras.Model(inputs, outputs)
        self.model.compile(
            loss="binary_crossentropy",
            optimizer='rmsprop',
            metrics=['accuracy']
        )
        print("Model built and compiled")

    def train(self, model_name):
        callbacks = [
            tf.keras.callbacks.EarlyStopping(patience=5),
            tf.keras.callbacks.ModelCheckpoint(filepath=f'{model_name}.keras'),
            tf.keras.callbacks.TensorBoard(log_dir='./logs'),
        ]
        history = self.model.fit(
            self.train_dataset,
            epochs=EPOCHS,
            validation_data=self.valid_dataset,
            callbacks=callbacks
        )

        # Plot training accuracy and loss
        acc = history.history['accuracy']
        loss = history.history['loss']
        plt.plot(range(1, len(acc) + 1), acc, label='Training Accuracy')
        plt.plot(range(1, len(loss) + 1), loss, label='Training Loss')
        plt.legend()
        plt.show()

    def load_model(self, model_name):
        self.model = tf.keras.models.load_model(model_name)

    def predict(self, image_file):
        img = tf.keras.utils.load_img(image_file, target_size=IMAGE_SHAPE[:2])
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, axis=0) / 255.0  # Normalize the image
        prediction = self.model.predict(img_array)
        predicted_class = CLASS_NAMES[int(prediction[0] > 0.5)]
        print(f"Predicted: {predicted_class}")
        plt.imshow(img)
        plt.title(f"Prediction: {predicted_class}")
        plt.axis('off')
        plt.show()
