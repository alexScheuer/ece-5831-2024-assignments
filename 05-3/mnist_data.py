import numpy as np
import sys
from PIL import Image, ImageOps
import urllib
import gzip
import pickle
import os
import matplotlib.pyplot as plt

class MnistData:
    image_size = 28*28
    dataset_dir = 'dataset'
    dataset_pkl = 'mnist.pkl'
    url_base = 'https://jrkwon.com/data/ece5831/mnist/'

    key_file = {
        'train_images': 'train-images-idx3-ubyte.gz',
        'train_labels': 'train-labels-idx1-ubyte.gz',
        'test_images':  't10k-images-idx3-ubyte.gz',
        'test_labels':  't10k-labels-idx1-ubyte.gz'
    }

    file_name = key_file['train_images']
    file_path = url_base + file_name
    
    def __init__(self, image_size):
        self.image_size = image_size
        self.url_base = 'https://jrkwon.com/data/ece5831/mnist/'

    def softmax(self, a):
        return np.exp(a) / np.sum(np.exp(a))

    def softmax_modified(self, a):
        c = np.max(a)
        exp_a = np.exp(a - c)
        return exp_a / np.sum(exp_a)

    def _load_images(self, file_name):
        with gzip.open(file_name, 'rb') as f:
            images = np.frombuffer(f.read(), np.uint8, offset=16)
        images = images.reshape(-1, self.image_size)
        return images

    def _load_labels(self, file_name):
        with gzip.open(file_name, 'rb') as f:
            labels = np.frombuffer(f.read(), np.uint8, offset=8)
        return labels

    def download(self, file_name):
        file_path = os.path.join(dataset_dir, file_name)

        if os.path.exists(file_path):
            print(f'File: {file_name} already exists')
            return

        print(f'Downloading {file_name}...')
        urllib.request.urlretrieve(self.url_base + file_name, file_path)

    def _download_all(self):
        for file_name in key_file.values():
            self.download(file_name)

    def change_one_hot_label(self, y, num_class, idx):
        t = np.zeros((y.size, num_class))
        for idx, row in enumerate(t):
            row[y[idx]] = 1
        return t

    def _create_dataset(self, key_file, dataset_dir, dataset_pkl, file_name1, file_name2, file_name3, file_name4):
        dataset = {}
        dataset[file_name1] = self._load_images(os.path.join(dataset_dir, key_file[file_name1]))
        dataset[file_name2] = self._load_labels(os.path.join(dataset_dir, key_file[file_name2]))
        dataset[file_name3] = self._load_images(os.path.join(dataset_dir, key_file[file_name3]))
        dataset[file_name4] = self._load_labels(os.path.join(dataset_dir, key_file[file_name4]))

        with open(os.path.join(dataset_dir, dataset_pkl), 'wb') as f:  # Change to 'wb'
            print(f'Pickle: {dataset_dir}/{dataset_pkl} is being created.')
            pickle.dump(dataset, f)
        
        return dataset

    def init_dataset(self, key_file, dataset_dir, dataset_pkl, file_name1, file_name2, file_name3, file_name4):
        self._download_all()
        if os.path.exists(os.path.join(dataset_dir, dataset_pkl)):
            with open(os.path.join(dataset_dir, dataset_pkl), 'rb') as f:
                dataset = pickle.load(f) 
        else:
            dataset = self._create_dataset(key_file, dataset_dir, dataset_pkl, file_name1, file_name2, file_name3, file_name4)
        
        return dataset

    def load_image(file_path):
        # Replace this with the path to your image
        image = Image.open(file_path).convert("RGB")
        return image

    def init():
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

    def load_my_model():
        # Load the model
        model = load_model("model/keras_model.h5")

        # Load the labels
        class_names = open("model/labels.txt", "r").readlines()

        return model, class_names

    def prep_input(image):
        # Create the array of the right shape to feed into the keras model
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Resize the image to be 224x224 and crop from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # Convert image to numpy array and normalize
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized_image_array

        return data

    def predict(model, class_names, data):
        # Make a prediction
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print the prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", confidence_score)
