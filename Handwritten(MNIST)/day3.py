from sklearn.datasets import fetch_openml
import matplotlib
import matplotlib.pyplot as plt

mnist = fetch_openml('mnist_784')
x,y = mnist['data'],mnist['target']
# print(mnist.target)
# print(x.shape)
# print(y.shape)
some_digit = x.iloc[3600].values
some_digit_image = some_digit.reshape(28, 28)
plt.imshow(some_digit_image, cmap='gray',interpolation='nearest')
plt.show()