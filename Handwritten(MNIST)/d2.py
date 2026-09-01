from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

mnist = fetch_openml("mnist_784")

X, y = mnist["data"], mnist["target"]
X_train = X[:60000]
X_test = X[60000:]

y_train = y[:60000]
y_test = y[60000:]
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("X_test:", X_test.shape)
print("y_test:", y_test.shape)


print("X shape:", X.shape)
print("y shape:", y.shape)

some_digit = X.iloc[0]

print("Pixels:", some_digit.shape)
print("Label:", y.iloc[0])

some_digit_image = some_digit.to_numpy().reshape(28, 28)

plt.imshow(some_digit_image, cmap="binary")
plt.title(f"Label: {y.iloc[0]}")
plt.axis("off")
# for i in range(10):
#     print(i, y.iloc[i])
plt.show()