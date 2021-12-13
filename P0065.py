from re import VERBOSE
from numpy.core.overrides import verify_matching_signatures
from sklearn import datasets
import tensorflow as tf
from keras.models import load_model

iris = datasets.load_iris()

in_size = 4
nb_classes = 3

x = iris.data
y = tf.keras.utils.to_categorical(iris.target, nb_classes)

model = load_model('iris_model.h5')

model.load_weights('iris_weight.h5')

score = model.evaluate(x, y, verbose=1)

print("정답률=", score[1])