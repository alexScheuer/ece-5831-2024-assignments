import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from le_net import LeNet

def preprocess_custom_image(image_path):
    img = load_img(image_path, color_mode="grayscale", target_size=(28, 28))

    img_array = img_to_array(img) / 255.0

    img_array = img_array.reshape(28, 28, 1)

    return np.array([img_array])  # Return as a batch of size 1 for prediction

def main():
    if len(sys.argv) != 3:
        print("Usage: python module8.py <image_filename> <actual_digit>")
        sys.exit(1)

    image_filename = sys.argv[1]
    actual_digit = int(sys.argv[2])

    # Create a LeNet instance and load the trained model
    lenet_loaded = LeNet()
    lenet_loaded.load("scheuer_cnn_model")  # Load the saved model

    custom_image = preprocess_custom_image(image_filename)

    predicted_digit = lenet_loaded.predict(custom_image)[0]

    # Show the input image using imshow
    img = load_img(image_filename, color_mode="grayscale")
    plt.imshow(img, cmap="gray")
    plt.title(f"Input Image: {image_filename}")
    plt.axis("off")
    plt.show()

    if predicted_digit == actual_digit:
        print(f"Success: Image {image_filename} is for digit {actual_digit} and is recognized as {predicted_digit}.")
    else:
        print(f"Fail: Image {image_filename} is for digit {actual_digit} but the inference result is {predicted_digit}.")

if __name__ == "__main__":
    main()
