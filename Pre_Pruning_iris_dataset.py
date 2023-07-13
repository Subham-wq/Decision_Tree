from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier with pre-pruning parameters
dt = DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_split=10, random_state=42)

# Fit the decision tree classifier to the training data
dt.fit(X_train, y_train)

# Evaluate the model on the testing data
y_pred = dt.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}".format(accuracy))

# Plot the decision tree
plot_tree(dt, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
