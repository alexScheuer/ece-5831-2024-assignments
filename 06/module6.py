import argparse
import numpy as np
import sys
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image, ImageOps
from keras.models import load_model
import os

class MnistData:
    def load_image(self, file_path):
        try:
            image = Image.open(file_path).convert("L")  # Convert to grayscale
            return image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def prep_input(self, image):
        # Resize to 28x28 for MNIST model and normalize
        image = ImageOps.fit(image, (28, 28), Image.Resampling.LANCZOS)
        image_array = np.asarray(image) / 255.0  # Normalize to [0, 1]
        image_array = image_array.reshape(1, 28, 28, 1)  # Shape for model input
        return image_array

    def load_my_model(self):
        try:
            model = tf.keras.models.load_model("model/scheuer_model.h5")
            #model = load_model("model/keras_model.h5")
            with open("model/labels.txt", "r") as f:
                class_names = f.read().splitlines()
            return model, class_names
        except Exception as e:
            print(f"Error loading model or labels: {e}")
            return None, None

def main():
    parser = argparse.ArgumentParser(description='Predict digit in an image file')
    parser.add_argument('image_file', type=str, help='Path to the image file')
    parser.add_argument('actual_digit', type=int, help='Actual digit of the image')
    args = parser.parse_args()

    mnist_data = MnistData()

    # Load the image
    image = mnist_data.load_image(args.image_file)
    if image is None:
        print("Failed to load image.")
        return

    # Preprocess the image for model input
    data = mnist_data.prep_input(image)

    # Load the model and class names
    model, class_names = mnist_data.load_my_model()
    if model is None or class_names is None:
        print("Failed to load model or labels.")
        return

    # Show the input image
    plt.imshow(image, cmap='gray')
    plt.title(f'Input Image: {args.image_file}')
    plt.axis('off')
    plt.show()

    # Predict the digit using the model
    try:
        prediction = model.predict(data)
        predicted_digit = np.argmax(prediction)
        confidence_score = prediction[0][predicted_digit]
    except Exception as e:
        print(f"Error during prediction: {e}")
        return

    # Display success/fail message based on prediction
    if predicted_digit == args.actual_digit:
        print(f"Success: Image {args.image_file} is for digit {args.actual_digit} and was recognized as {predicted_digit} with confidence {confidence_score:.2f}.")
    else:
        print(f"Fail: Image {args.image_file} is for digit {args.actual_digit} but was recognized as {predicted_digit} with confidence {confidence_score:.2f}.")

if __name__ == "__main__":
    main()
