# MNIST - Hello World for ML
import numpy as np
import urllib
import gzip
import pickle
import os
import matplotlib.pyplot as plt

class MnistData:
    image_size = 28 * 28
    dataset_dir = 'dataset'
    dataset_pkl = 'mnist.pkl'
    url_base = 'https://jrkwon.com/data/ece5831/mnist/'

    key_file = {
        'train_images': 'train-images-idx3-ubyte.gz',
        'train_labels': 'train-labels-idx1-ubyte.gz',
        'test_images':  't10k-images-idx3-ubyte.gz',
        'test_labels':  't10k-labels-idx1-ubyte.gz'
    }
    
    def __init__(self):
        self.image_size = 28 * 28

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
        file_path = os.path.join(self.dataset_dir, file_name)

        if os.path.exists(file_path):
            print(f'File: {file_name} already exists')
            return

        print(f'Downloading {file_name}...')
        urllib.request.urlretrieve(self.url_base + file_name, file_path)

    def _download_all(self):
        for file_name in self.key_file.values():
            self.download(file_name)

    def _create_dataset(self):
        dataset = {}
        dataset['train_images'] = self._load_images(os.path.join(self.dataset_dir, self.key_file['train_images']))
        dataset['train_labels'] = self._load_labels(os.path.join(self.dataset_dir, self.key_file['train_labels']))
        dataset['test_images'] = self._load_images(os.path.join(self.dataset_dir, self.key_file['test_images']))
        dataset['test_labels'] = self._load_labels(os.path.join(self.dataset_dir, self.key_file['test_labels']))

        with open(os.path.join(self.dataset_dir, self.dataset_pkl), 'wb') as f:
            print(f'Pickle: {self.dataset_dir}/{self.dataset_pkl} is being created.')
            pickle.dump(dataset, f)
        
        return dataset

    def init_dataset(self):
        self._download_all()
        if os.path.exists(os.path.join(self.dataset_dir, self.dataset_pkl)):
            with open(os.path.join(self.dataset_dir, self.dataset_pkl), 'rb') as f:
                dataset = pickle.load(f) 
        else:
            dataset = self._create_dataset()
        
        return dataset

    def load(self):
        # Load the dataset
        dataset = self.init_dataset()
        
        # One-hot encode the labels
        num_classes = 10  # MNIST has 10 classes (digits 0-9)
        train_labels = self.change_one_hot_label(dataset['train_labels'], num_classes)
        test_labels = self.change_one_hot_label(dataset['test_labels'], num_classes)

        # Return the train and test datasets
        return (dataset['train_images'], train_labels), (dataset['test_images'], test_labels)

    def change_one_hot_label(self, y, num_class):
        t = np.zeros((y.size, num_class))
        for idx, row in enumerate(t):
            row[y[idx]] = 1
        return t

# Example usage:
if __name__ == "__main__":
    mnist_data = MnistData()
    (train_images, train_labels), (test_images, test_labels) = mnist_data.load()
    print("Loaded dataset:")
    print("Train images shape:", train_images.shape)
    print("Train labels shape:", train_labels.shape)
    print("Test images shape:", test_images.shape)
    print("Test labels shape:", test_labels.shape)
