from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
mnist = fetch_openml("mnist_784")

x, y = mnist["data"], mnist["target"]

# Split dataset
x_train = x[:60000]
x_test = x[60000:]

y_train = y[:60000]
y_test = y[60000:]

# 5 vs not-5
y_train_5 = (y_train == "5")
y_test_5 = (y_test == "5")

# Create model
sgd_clf = SGDClassifier(random_state=42)

# Train model
sgd_clf.fit(x_train, y_train_5)

# Test one image
some_digit = x.iloc[0]

prediction = sgd_clf.predict([some_digit])



y_pred = sgd_clf.predict(x_test)
accuracy = accuracy_score(y_test_5, y_pred)
print(y_pred)
print(y_test_5)
print("Prediction:", prediction)
print("Actual:", y.iloc[0])
print("Accuracy:", accuracy)