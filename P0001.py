import tensorflow as tf
from tensorflow import keras
print("tensorflow version : ", tf.__version__)
fashion_data = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_data.load_data()
