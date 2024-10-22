# module5-2.py
import argparse
import matplotlib.pyplot as plt
from mnist_data import MnistData

def main(dataset_type, index):
    myMnistData = MnistData()
    (train_images, train_labels), (test_images, test_labels) = myMnistData.load()

    if dataset_type == 'train':
        images = train_images
        labels = train_labels
    elif dataset_type == 'test':
        images = test_images
        labels = test_labels
    else:
        print("Invalid dataset type. Use 'train' or 'test'.")
        return

    if index < 0 or index >= len(images):
        print("Index out of bounds.")
        return

    # Display the image
    plt.imshow(images[index].reshape(28, 28), cmap='gray')
    plt.title(f'Label: {np.argmax(labels[index])}')  # Assuming labels are one-hot encoded
    plt.show()

    # Print the label
    print(f'Label: {np.argmax(labels[index])}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display MNIST images.')
    parser.add_argument('dataset_type', type=str, help='Type of dataset (train or test)')
    parser.add_argument('index', type=int, help='Index of the dataset image')
    
    args = parser.parse_args()
    main(args.dataset_type, args.index)
