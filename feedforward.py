# import necessary libraries
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

# load the iris dataset
iris = load_iris()

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)

# convert labels to one-hot vectors
y_train = to_categorical(y_train, 3)
y_test = to_categorical(y_test, 3)

# create a feedforward neural network
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

# compile the model
sgd = SGD(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# train the model
model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=1)

# evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1] * 100))